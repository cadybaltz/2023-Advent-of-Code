"""
cadybaltz
12/05/2023
AoC 2023 Day 5
Part 1: 171, 00:03:15
Part 2: 344, 00:09:56
"""

import sys

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

        if new_start > end + value or new_end < start + value:
            # Check if the new tuple does not overlap with any existing tuple in result
            new_result.append([start, end, value, False])
        else:
            # Take the overlapping part from the new tuple and add it to the existing tuple
            overlapping_start = max(start + value, new_start)
            overlapping_end = min(end + value, new_end)

            new_result.append([overlapping_start - value, overlapping_end - value, value + new_value, True])

            g = start + value
            h = end + value

            if g < new_start:
                if h < new_start:
                    new_result.append([g - value, h - value, value, False])
                elif h <= new_end:
                    new_result.append([g - value, new_start - 1 - value, value, False])
                    new_result.append([new_start - value, h - value, value + new_value, True])
                else:
                    new_result.append([g - value, new_start - 1 - value, value, False])
                    new_result.append([new_start - value, new_end - value, value + new_value, True])
                    new_result.append([new_end + 1 - value, h - value, value, False])
            elif g <= new_end:
                if h <= new_end:
                    new_result.append([g - value, h - value, value + new_value, True])
                else:
                    new_result.append([g - value, new_end - value, value + new_value, True])
                    new_result.append([new_end + 1 - value, h - value, value, False])
            else:
                new_result.append([g - value, h - value, value, False])
    new_new_res = []
    seen = {}
    for val in new_result:
        key = str(val[0])+','+str(val[1])+','+str(val[3])
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
    return sorted(new_new_res, key=lambda tup: tup[0]), seen

def combine_overlapping_ranges(ranges):
    result = []
    for start, end in sorted(ranges):
        if result and start <= result[-1][1] + 1:
            result[-1] = (result[-1][0], max(result[-1][1], end))
        else:
            result.append((start, end))
    return result


# given old list of tuples
# add new
def method2(existing_tuples, new_tuple):

    curr = new_tuple
    currs = []

    x = 0
    while x < len(existing_tuples):
        existing_tuple = existing_tuples[x]
        if curr is not None:
            if existing_tuple[1] < curr[0]:
                if x == len(existing_tuples) - 1:
                    currs.append(curr)
                    curr = None
            elif curr[0] < existing_tuple[0]:
                if curr[1] > existing_tuple[0]:
                    currs.append((curr[0], existing_tuple[0] - 1, curr[2]))
                    curr = (existing_tuple[1] + 1, curr[1], curr[2])

                else:
                    currs.append(curr)
                    curr = None

            elif curr[0] >= existing_tuple[0]:
                if curr[1] > existing_tuple[1]:
                    curr = (existing_tuple[1] + 1, curr[1], curr[2])
                else:
                    curr = None

        x += 1

    if curr is not None:
        currs.append(curr)
    for curr in currs:
        existing_tuples.append(curr)
    return sorted(existing_tuples, key=lambda tup: tup[0])


def solution(file):
    lines = file.readlines()

    result = 0

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
        nt_seen = set()

        # for the existing tuples. if after they are modified, they match the next step, update the change value.
        n = 0

        sortedd = sorted(maps[b], key=lambda tup: tup[0])
        while n < len(sortedd):
            other = sortedd[n]

            new, nt_seen = method1(num_transform, other, set())
            num_transform = sorted(new, key=lambda tup: tup[0])
            n += 1

        for r in num_transform:
            r[3] = False
        num_transform = sorted(num_transform, key=lambda tup: tup[0])
        print(num_transform)

    mini = 100000000000000000


    for nt in num_transform:
        if nt[0] + nt[2] > 0:
            mini = min(mini, nt[0] + nt[2])
        if nt[1] + nt[2] > 0:
            mini = min(mini, nt[1] + nt[2])

    return mini


if __name__ == '__main__':
    if sys.argv[1] == 't':
        input = open("test.txt", "r")
    else:
        input = open("input.txt", "r")
    print(solution(input))

# too low: 30202489
