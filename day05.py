"""
cadybaltz
12/05/2023
AoC 2023 Day 5
Part 1: 2690, 00:28:13
Part 2: 38643, 20:18:11
"""

import sys

def solution_pt1(file):
    lines = file.readlines()

    seeds = []

    all_maps = []
    curr_map = {}

    x = 0
    while x < len(lines):
        line = lines[x]

        if x == 0:
            seed_l = line.split()
            for y in range(1, len(seed_l)):
                seeds.append(seed_l[y])
        elif x >= 3:
            if len(line) < 3:
                all_maps.append(curr_map)
                curr_map = {}
                x += 1
            else:
                curr = line.split()
                range1 = int(curr[2])

                curr_map[(int(curr[1]), int(curr[1]) + range1 - 1)] = int(curr[0]) - int(curr[1])
        x += 1
        all_maps.append(curr_map)

    min = sys.maxsize
    for seed in seeds:
        new_curr = None
        curr = int(seed)
        for maps in all_maps:
            for r, v in maps.items():
                if r[0] <= curr <= r[1]:
                    new_curr = curr + v
            if new_curr is not None:
                curr = new_curr

        if curr < min:
            min = curr

    return min

def method1(sorted_list, new_tuple, seen):
    new_result = []
    new_start, new_end, new_value = new_tuple

    for i, lt in enumerate(sorted_list):
        start = lt[0]
        end = lt[1]
        value = lt[2]
        is_done = lt[3]

        if is_done:
            new_result.append(lt)

        if new_end < start + value:
            new_result.append([start, end, value, False])
        else:
            g = start + value
            h = end + value
            offset_g = g - value
            offset_h = h - value

            if g < new_start:
                if h < new_start:
                    new_result.append([offset_g, offset_h, value, True])
                elif h <= new_end:
                    new_result.append([offset_g, new_start - 1 - value, value, True])
                    new_result.append([new_start - value, offset_h, value + new_value, True])
                else:
                    new_result.append([offset_g, new_start - 1 - value, value, True])
                    new_result.append([new_start - value, new_end - value, value + new_value, True])
                    new_result.append([new_end + 1 - value, offset_h, value, False])
            elif g <= new_end:
                if h <= new_end:
                    new_result.append([offset_g, offset_h, value + new_value, True])
                else:
                    new_result.append([offset_g, new_end - value, value + new_value, True])
                    new_result.append([new_end + 1 - value, offset_h, value, False])
            else:
                new_result.append([offset_g, offset_h, value, False])
    new_new_res = []
    seen = {}
    for val in new_result:
        key = str(val[0]) + ',' + str(val[1]) + ',' + str(val[3])
        key1 = str(val[0]) + ',' + str(val[1]) + ',' + "True"
        key2 = str(val[0]) + ',' + str(val[1]) + ',' + "False"
        if(val[3]):
            if key2 in seen:
                if [val[0],val[1],seen[key2],False] in new_new_res:
                    new_new_res.remove([val[0],val[1],seen[key2],False])
            if key not in seen:
                new_new_res.append(val)
                seen[key] = val[2]
        else:
            if key1 in seen or key in seen:
                continue
            else:
                seen[key] = val[2]
                new_new_res.append(val)
    return sorted(new_new_res, key=lambda tup: tup[0])

def solution_pt2(file):
    lines = file.readlines()

    seed_ranges = []

    maps = []
    curr_map = []

    x = 0
    while x < len(lines):
        line = lines[x]

        if x == 0:
            seed_l = line.split()
            y = 1
            while y < len(seed_l):
                seed_ranges.append((int(seed_l[y]), int(seed_l[y]) + int(seed_l[y + 1]) - 1))
                y += 2

        else:
            if len(line) < 3:
                maps.append(curr_map)
                curr_map = []
                x += 1
            else:
                curr = line.split()
                range1 = curr[2]

                curr_map.append((int(curr[1]), int(curr[1]) + int(range1) - 1, int(curr[0]) - int(curr[1])))
        x += 1

    maps.append(curr_map)

    num_transform = []
    for sr in seed_ranges:
        num_transform.append([sr[0], sr[1], 0, False])

    for b in range(1, len(maps)):
        n = 0

        sortedd = sorted(maps[b], key=lambda tup: tup[0])
        while n < len(sortedd):
            other = sortedd[n]

            new = method1(num_transform, other, set())
            num_transform = sorted(new, key=lambda tup: tup[0])
            n += 1

        for r in num_transform:
            r[3] = False
        num_transform = sorted(num_transform, key=lambda tup: tup[0])

    mini = sys.maxsize
    new_min = set()
    for nt in num_transform:
        mini = min(mini, nt[0] + nt[2])
        mini = min(mini, nt[1] + nt[2])
        if mini not in new_min:
            new_min.add(mini)

    # this produces a set of four numbers for my input.txt. one of them is the correct answer, and it's not the lowest number.
    # why? no one will ever know.
    return new_min


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