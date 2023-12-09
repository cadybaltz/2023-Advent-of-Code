"""
cadybaltz
12/09/2023
AoC 2023 Day 9
Part 1: 559, 00:07:04
Part 2: 765, 00:10:57
"""

import sys

def solution(file):
    lines = file.readlines()

    pt_1_result = 0
    pt_2_result = 0

    for x in range(len(lines)):
        line = lines[x]

        string_vals = line.split()
        int_vals = []
        for d in string_vals:
            int_vals.append(int(d))

        sequences = [int_vals]
        curr = int_vals

        all_zero = False
        while not all_zero:
            new_seq = []
            for y in range(len(curr) - 1):
                new_seq.append(curr[y+1] - curr[y])

            all_zero = True
            for val in new_seq:
                if val != 0:
                    all_zero = False

            sequences.append(new_seq)
            curr = new_seq

        tot = 0
        for l in reversed(sequences):
            tot += l[len(l)-1]
        pt_1_result += tot

        prev = 0
        for sequence in reversed(sequences):
            prev = sequence[0] - prev
        pt_2_result += prev

    return pt_1_result, pt_2_result


if __name__ == '__main__':
    if sys.argv[1] == 't':
        input = open("test.txt", "r")
    else:
        input = open("input.txt", "r")
    print(solution(input))
