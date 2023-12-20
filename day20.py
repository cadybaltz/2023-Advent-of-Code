"""
cadybaltz
12/16/2023
AoC 2023 Day 16
Part 1: 849, 00:22:15
Part 2: 666, 00:26:26
"""

import sys
from queue import Queue


def solution(lines):
    result = 0
    h = 0
    low = 0

    a = {}
    b = {}
    queue = []
    on = {}
    inputs = {}
    for x in range(len(lines)):
        line = lines[x].strip()

        values = line.split()
        if values[0][0] == '%':
            a[values[0][1:]] = '%'
            b[values[0][1:]] = []
            for val in values[2:]:
                b[values[0][1:]].append(val.replace(',', '').replace(' ', ''))
            on[values[0][1:]] = False
        elif values[0][0] == '&':
            a[values[0][1:]] = '&'

            b[values[0][1:]] = []
            for val in values[2:]:
                b[values[0][1:]].append(val.replace(',', '').replace(' ', ''))

            inputs[values[0][1:]] = {}
        else:
            a[values[0]] = 'x'

            b[values[0]] = []
            for val in values[2:]:
                b[values[0]].append(val.replace(',', '').replace(' ', ''))
    print(b)

    for conj in inputs.keys():
        for k,v in b.items():
            for t in v:
                if t == conj:
                    inputs[conj][k] = 0

    res = 0
    cad_map = {}
    anbswer = {}
    while True:
        res += 1
        curr = 'broadcaster'
        qu = Queue()
        qu.put((curr, 0, None))

        while qu.qsize() > 0:
            next_v, next_p, last = qu.get()
            # print(next_v, next_p, last)
            if next_p == 0:
                low += 1
            else:
                h += 1

            if next_v == 'vd':
                for keycad, cad in inputs[next_v].items():
                    if cad == 1:
                        if keycad not in cad_map:
                            cad_map[keycad] = res
                        elif res > cad_map[keycad]:
                            anbswer[keycad] = res - cad_map[keycad]
                        if len(anbswer) == 4:
                            return anbswer


            if next_v not in a:
                if next_p == 0:
                    return res
                continue

            if a[next_v] == '%':
                if next_p == 0:
                    if on[next_v]:
                        on[next_v] = False
                        for cont in b[next_v]:
                            qu.put((cont, 0, next_v))
                    else:
                        on[next_v] = True
                        for cont in b[next_v]:
                            qu.put((cont, 1, next_v))
            elif a[next_v] == '&':
                inputs[next_v][last] = next_p
                all_high = True
                for n in inputs[next_v].values():
                    if not n:
                        all_high = False
                if all_high:
                    for cont in b[next_v]:
                        qu.put((cont, 0, next_v))
                else:
                    for cont in b[next_v]:
                        qu.put((cont, 1, next_v))
            else:
                for cont in b[next_v]:
                    qu.put((cont, next_p, next_v))

    return low * h


if __name__ == '__main__':
    if sys.argv[1] == 't':
        input = open("test.txt", "r")
    else:
        input = open("input.txt", "r")

    lines = input.readlines()

    print(solution(lines))


# 456600365373478
# 456600365373479
# 228300182686739