"""
cadybaltz
12/15/2023
AoC 2023 Day 15
Part 1: 2777, 00:08:02
Part 2: 2855, 00:35:33
"""

import sys

def solution(input):
    pt1_result = 0
    pt2_result = 0

    boxes_a = [[] for _ in range(256)]
    boxes_m = [{}] * 256

    inputs = input.strip().split(',')
    for input in inputs:
        input = input.strip()

        hash = 0

        key = ""
        x = 0
        while x < len(input) and input[x] != '=' and input[x] != '-':
            key += input[x]
            hash += ord(input[x])
            hash *= 17
            hash = hash % 256
            x += 1

        # part 1's hash function should process the rest of the input string
        pt1_x = x
        pt1_hash = hash
        while pt1_x < len(input):
            pt1_hash += ord(input[pt1_x])
            pt1_hash *= 17
            pt1_hash = pt1_hash % 256
            pt1_x += 1

        pt1_result += pt1_hash

        if '=' in input:
            value = input[x+1:]

            if key not in boxes_a[hash]:
                boxes_a[hash].append(key)
            boxes_m[hash][key] = value

        else:
            if key in boxes_m[hash].keys():
                del boxes_m[hash][key]
                boxes_a[hash].remove(key)

    for x in range(len(boxes_a)):
        if len(boxes_a[x]) >= 1:
            for y in range(len(boxes_a[x])):
                pt2_result += (x + 1) * (y + 1) * int((boxes_m[x][boxes_a[x][y]]))

    return pt1_result, pt2_result


if __name__ == '__main__':
    if sys.argv[1] == 't':
        input = open("test.txt", "r")
    else:
        input = open("input.txt", "r")

    lines = input.readlines()
    a, b = solution(lines[0])
    print("Part 1: " + str(a))
    print("Part 2: " + str(b))
