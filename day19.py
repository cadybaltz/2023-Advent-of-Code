"""
cadybaltz
12/19/2023
AoC 2023 Day 19
Part 1: 1292, 00:26:29
Part 2: 11749, 15:29:59
"""
import copy
import sys
import re
xmas = list('xmas')

def rec(curr_workflow, workflows, ranges):
    total = 0
    for range in ranges:
        if len(range) == 0:
            return

    if curr_workflow == 'R':
        return 0
    elif curr_workflow == 'A':
        result = 1
        for val in xmas:
            if len(ranges[val]) == 0:
                result = 0
            else:
                result *= ranges[val][len(ranges[val]) - 1][1] - (ranges[val][0][0] - 1)
        return result

    for step in workflows[curr_workflow]:
        if ':' in step:
            next = step.split(':')[1]

            if '<' in step:
                letter = step.split('<')[0]
                number = step.split('<')[1].split(':')[0]
                def compare(a,b):
                    return a < b

            elif '>' in step:
                letter = step.split('>')[0]
                number = step.split('>')[1].split(':')[0]
                def compare(a,b):
                    return a > b

            new_ranges = copy.deepcopy(ranges)
            new_range = []
            for range in ranges[letter]:
                if compare(int(range[1]), int(number)):
                    new_range.append(range)
            for range in new_range:
                ranges[letter].remove(range)
            new_ranges[letter] = new_range
            total += rec(next, workflows, new_ranges)

        else:
            total += rec(step, workflows, ranges)

    return total

def solution(lines):
    found_blank = False
    workflows = {}

    pt1_ratings = []
    
    for x in range(len(lines)):
        line = lines[x].strip()
        if len(line) == 0:
            found_blank = True
        elif not found_blank:
            key = line.split('{', 1)[0]
            pattern = r'[a-zA-Z]+[<>]\d+:[a-zA-Z]+|R|A|[a-zA-Z]+'
            matches = re.findall(pattern, line)
            workflows[key] = matches[1:]
        else:
            pattern = r'x=(\d+),m=(\d+),a=(\d+),s=(\d+)'
            match = re.search(pattern, line)
            groups = match.groups()
            pt1_ratings.append(groups)

    ranges = {}
    for x in xmas:
        ranges[x] = []

    for workflow in workflows.values():
        for w in range(len(workflow)):
            if '>' in workflow[w]:
                pattern = r'>|:'
                vals = re.split(pattern, workflow[w])
                ranges[vals[0]].append(int(vals[1]) + 1)
                ranges[vals[0]].append(int(vals[1]))
            elif '<' in workflow[w]:
                pattern = r'<|:'
                vals = re.split(pattern, workflow[w])
                ranges[vals[0]].append(int(vals[1]))
                ranges[vals[0]].append(int(vals[1]) - 1)

    for val in xmas:
        ranges[val].append(0)
        ranges[val].append(4000)
        ranges[val].sort()
        new_ranges = []
        for r in range(1,len(ranges[val])):
            new_ranges.append((ranges[val][r-1]+1,ranges[val][r]))
        ranges[val] = new_ranges

    return rec('in', workflows, ranges)

if __name__ == '__main__':
    if sys.argv[1] == 't':
        input = open("test.txt", "r")
    else:
        input = open("input.txt", "r")

    lines = input.readlines()
    print(solution(lines))