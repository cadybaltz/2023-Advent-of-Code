"""
cadybaltz
12/08/2023
AoC 2023 Day 8
Part 1: 6014, 00:20:54
Part 2: 3101, 00:43:09
"""

import sys
import re
import math


def solution_pt1(file):
    lines = file.readlines()

    result = 0

    lr_list = lines[0].strip()
    mapping = {}
    for x in range(2, len(lines)):
        line = lines[x]

        pattern = r'([A-Za-z0-9]+)\s*=\s*\(([A-Za-z0-9]+),\s*([A-Za-z0-9]+)\)'
        match = re.match(pattern, line)
        groups = match.groups()

        mapping[groups[0]] = (groups[1], groups[2])

    x = 0
    curr = 'AAA'
    while x < len(lr_list):
        result += 1
        d = lr_list[x]

        if d == 'R':
            curr = mapping[curr][1]
        if d == 'L':
            curr = mapping[curr][0]

        if curr == 'ZZZ':
            return result

        x += 1
        if x == len(lr_list):
            x = 0

    return result


def lcm(nums):
    curr = nums[0]
    for num in nums[1:]:
        curr = math.lcm(curr, num)
    return curr


def solution_pt2(file):
    lines = file.readlines()

    result = 0

    lr_list = lines[0].strip()
    mapping = {}
    starts = []
    for x in range(2, len(lines)):
        line = lines[x]

        pattern = r'([A-Za-z0-9]+)\s*=\s*\(([A-Za-z0-9]+),\s*([A-Za-z0-9]+)\)'
        match = re.match(pattern, line)
        groups = match.groups()

        mapping[groups[0]] = (groups[1], groups[2])
        if groups[0][2] == 'A':
            starts.append(groups[0])

    found_z_time = []
    for x in range(len(starts)):
        found_z_time.append([])

    x = 0
    currs = starts.copy()
    while x < len(lr_list):
        result += 1
        new_currs = []
        for y in range(len(starts)):
            curr = currs[y]
            d = lr_list[x]

            if d == 'R':
                new_curr = mapping[curr][1]
            if d == 'L':
                new_curr = mapping[curr][0]

            new_currs.append(new_curr)

            if new_curr[2] == 'Z':
                found_z_time[y].append(result)

        currs = new_currs

        # once you have found 'Z' twice for each start, you can calculate the answer
        all_found_twice = True
        for val in found_z_time:
            if len(val) < 2:
                all_found_twice = False

        if all_found_twice:
            cycle_lengths = []
            for val in found_z_time:
                cycle_lengths.append(val[1] - val[0])
            return lcm(cycle_lengths)

        x += 1
        if x == len(lr_list):
            x = 0

    return result


if __name__ == '__main__':
    if sys.argv[1] == 't':
        input = open("test.txt", "r")
    else:
        input = open("input.txt", "r")
    print(solution_pt1(input))

    if sys.argv[1] == 't':
        input = open("test.txt", "r")
    else:
        input = open("input.txt", "r")
    print(solution_pt2(input))
