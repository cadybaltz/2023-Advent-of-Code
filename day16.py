"""
cadybaltz
12/16/2023
AoC 2023 Day 16
Part 1: 849, 00:22:15
Part 2: 666, 00:26:26
"""

import sys
from enum import Enum

class Dir(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

def solution(lines, start, dir):
    result = 0
    grid = []
    grid_seen = []

    for x in range(len(lines)):
        line = lines[x].strip()
        grid.append(list(line))

        i = []
        for y in range(len(line)):
            i.append(set())

        grid_seen.append(i)

    rays = [(start[0],start[1],dir)]

    while len(rays) >= 1:
        ray = rays.pop()

        hor = ray[2] == Dir.EAST or ray[2] == Dir.WEST
        ver = ray[2] == Dir.NORTH or ray[2] == Dir.SOUTH
        
        dir = {
            Dir.NORTH: (-1,0),
            Dir.EAST: (0,1),
            Dir.SOUTH: (1,0),
            Dir.WEST: (0,-1)
        }

        new_x = ray[0] + dir[ray[2]][0]
        new_y = ray[1] + dir[ray[2]][1]

        if not 0 <= new_x < len(grid) or not 0 <= new_y < len(grid[0]):
            continue

        # no need to keep processing if you have already energized this space
        seen = ray[2] in grid_seen[new_x][new_y]

        grid_seen[new_x][new_y].add(ray[2])

        backslash = {
            Dir.NORTH: Dir.WEST,
            Dir.EAST: Dir.SOUTH,
            Dir.SOUTH: Dir.EAST,
            Dir.WEST: Dir.NORTH
        }

        forward = {
            Dir.NORTH: Dir.EAST,
            Dir.EAST: Dir.NORTH,
            Dir.SOUTH: Dir.WEST,
            Dir.WEST: Dir.SOUTH
        }

        if not seen:
            if grid[new_x][new_y] == "|" and not ver:
                rays.append((new_x, new_y, Dir.NORTH))
                rays.append((new_x, new_y, Dir.SOUTH))
            elif grid[new_x][new_y] == "-" and not hor:
                rays.append((new_x, new_y, Dir.EAST))
                rays.append((new_x, new_y, Dir.WEST))
            elif grid[new_x][new_y] == "/":
                rays.append((new_x, new_y, forward[ray[2]]))
            elif grid[new_x][new_y] == "\\":
                rays.append((new_x, new_y, backslash[ray[2]]))
            else:
                rays.append((new_x, new_y, ray[2]))




    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if len(grid_seen[x][y]) >= 1:
                result += 1


    return result


if __name__ == '__main__':
    if sys.argv[1] == 't':
        input = open("test.txt", "r")
    else:
        input = open("input.txt", "r")

    lines = input.readlines()

    print("Part 1: " + str(solution(lines, (0, -1), Dir.EAST)))

    maxi = 0
    for y in range(len(lines[0])):
        maxi = max(maxi, solution(lines, (-1, y), Dir.SOUTH))
        maxi = max(maxi, solution(lines, (len(lines), y), Dir.NORTH))

    for x in range(len(lines)):
        maxi = max(maxi, solution(lines, (x, -1), Dir.EAST))
        maxi = max(maxi, solution(lines, (x, len(lines[0])), Dir.WEST))

    print("Part 2: " + str(maxi))

