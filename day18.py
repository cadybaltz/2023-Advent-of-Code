"""
cadybaltz
12/18/2023
AoC 2023 Day 18
Part 1: 3703, 01:07:44
Part 2: 18350, >24h
"""

import sys

dir = {
    'R': (0,1),
    'L': (0,-1),
    'U': (-1,0),
    'D': (1,0)
}

hex_order = ['R', 'D', 'L', 'U']

def solution(lines, part):
    curr = (0,0)
    points = [(0,0)]
    v = 0
    h = 0

    for x in range(len(lines)):
        line = lines[x].strip()
        info = line.split()

        if (part == 1):
            letter = info[0]
            change = dir[letter]
            dist = int(info[1])
        else:
            letter = hex_order[int(info[2][7])]
            change = dir[letter]
            dist = int(info[2][2:7], 16)

        if letter == 'D':
            v+=dist
        if letter == 'L':
            h+=dist

        new_point = (int(curr[0]) + (int(change[0]) * dist), int(curr[1]) + (int(change[1]) * dist))
        points.append(new_point)
        curr = new_point
        
    # run shoelace algorithm
    a = 0
    b = 0
    for i in range(0,len(points)-1):
        a = a + points[i][0] *  points[i+1][1]
        b = b + points[i][1] *  points[i+1][0]
    
    area = abs(a - b) / 2
    return area + h + v + 1


if __name__ == '__main__':
    if sys.argv[1] == 't':
        input = open("test.txt", "r")
    else:
        input = open("input.txt", "r")

    lines = input.readlines()

    print("Part 1: " + str(solution(lines, 1)))
    print("Part 2: " + str(solution(lines, 2)))

