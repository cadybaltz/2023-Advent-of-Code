"""
cadybaltz
12/20/2023
AoC 2023 Day 20
Part 1: 86, 00:22:40
Part 2: 97, 00:48:30
"""
import math
import sys
from queue import Queue


def solution(lines):
    high = 0
    low = 0

    types = {}
    outputs = {}
    on = {}
    inputs = {}
    
    for x in range(len(lines)):
        line = lines[x].strip()

        values = line.split()

        module = values[0]
        first = module[0]
        if first == '%' or first == '&':
            module = module[1:]
            types[module] = first
            if first == '%':
                # flip-flops start in 'off' state
                on[module] = False

            else:
                # conjunctions must store inputs
                inputs[module] = {}

        else:
            types[module] = None

        outputs[module] = []
        for val in values[2:]:
            outputs[module].append(val.replace(',', ''))

    # find all inputs for each conjunction
    for conj in inputs.keys():
        for k, v in outputs.items():
            for output in v:
                if output == conj:
                    # remember all inputs as low pulse to start
                    inputs[conj][k] = 0
    cycle = {}
    cycle_lengths = {}

    pt1_count = 0
    pt2_answer = None
    count = 0

    while pt1_count < 1000 or pt2_answer is None:
        count += 1
        curr = 'broadcaster'
        qu = Queue()
        qu.put((curr, 0, None))

        while qu.qsize() > 0:
            next_v, next_p, last_v = qu.get()

            # check if the pulse is low or high
            if pt1_count < 1000:
                if next_p == 0:
                    low += 1
                else:
                    high += 1

            # manually checked my input to see what module sends a pulse to rx
            # &vd -> rx
            if next_v == 'vd':
                for input_v, input_p in inputs[next_v].items():
                    if input_p == 1:
                        if input_v not in cycle:
                            cycle[input_v] = count
                        elif count > cycle[input_v]:
                            cycle_lengths[input_v] = count - cycle[input_v]

                        # found cycle lengths for all inputs to 'vd'
                        if len(cycle_lengths) == len(inputs[next_v]):
                            pt2_answer = 1

                            # calculate LCM of all inputs to find the first cycle they will all be high pulses
                            for length in cycle_lengths.values():
                                pt2_answer = math.lcm(pt2_answer, int(length))

            # only hit for rx
            if next_v not in types:
                continue

            if types[next_v] == '%':

                # flip flop logic
                if next_p == 0:
                    if on[next_v]:
                        on[next_v] = False
                        for cont in outputs[next_v]:
                            qu.put((cont, 0, next_v))
                    else:
                        on[next_v] = True
                        for cont in outputs[next_v]:
                            qu.put((cont, 1, next_v))

            elif types[next_v] == '&':

                # update the current input pulse
                inputs[next_v][last_v] = next_p

                # check if all the inputs are remembered as high pulses
                all_high = True
                for n in inputs[next_v].values():
                    if not n:
                        all_high = False
                if all_high:
                    for cont in outputs[next_v]:
                        qu.put((cont, 0, next_v))
                else:
                    for cont in outputs[next_v]:
                        qu.put((cont, 1, next_v))
            else:
                for cont in outputs[next_v]:
                    qu.put((cont, next_p, next_v))
        pt1_count += 1

    print(low,high)
    return low * high, pt2_answer


if __name__ == '__main__':
    if sys.argv[1] == 't':
        input = open("test.txt", "r")
    else:
        input = open("input.txt", "r")

    lines = input.readlines()
    solution = solution(lines)

    print("Part 1: " + str(solution[0]))
    print("Part 2: " + str(solution[1]))
