"""
cadybaltz
12/06/2023
AoC 2023 Day 6
Part 1: 478, 00:04:57
Part 2: 227, 00:06:04
"""

import sys

# note: I modified my input.txt directly to remove the extra spaces for part 2. I also removed the words "Time:" and "Distance:"
def solution(file):
    lines = file.readlines()

    times = lines[0].split()
    dist = lines[1].split()

    res = 1

    for x in range(len(times)):
        # process each race
        ct = 0
        for t in range(int(times[x])):
            speed = t
            ttm = int(times[x]) - t
            total = ttm * speed
            if total > int(dist[x]):
                ct += 1
        res *= ct
    return res


if __name__ == '__main__':
    if sys.argv[1] == 't':
        input = open("test.txt", "r")
    else:
        input = open("input.txt", "r")
    print(solution(input))
