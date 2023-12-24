"""
cadybaltz
12/23/2023
AoC 2023 Day 21
Part 1: 2212, 00:21:35
Part 2: 10842, >24h
"""

import sys
import math
from collections import deque

def check_neighbors(grid, row, col, target, offset):
    neighbors = []

    # Check up
    if row > 0 and grid[row - 1][col] in target:
        neighbors.append((row - 1, col, offset))

    elif row == 0:
        if grid[len(grid) - 1][col] in target:
            neighbors.append((len(grid) - 1, col, (offset[0] + 1, offset[1])))

    # Check down
    if row < len(grid) - 1 and grid[row + 1][col] in target:
        neighbors.append((row + 1, col, offset))

    elif row == len(grid) - 1:
        if grid[0][col] in target:
            neighbors.append((0, col, (offset[0] - 1, offset[1])))

    # Check left
    if col > 0 and grid[row][col - 1] in target:
        neighbors.append((row, col - 1, offset))

    elif col == 0:
        if grid[row][len(grid[0]) - 1] in target:
            neighbors.append((row, len(grid[0]) - 1, (offset[0], offset[1] + 1)))

    # Check right
    if col < len(grid[0]) - 1 and grid[row][col + 1] in target:
        neighbors.append((row, col + 1, offset))

    elif col == len(grid[0]) - 1:
        if grid[row][0] in target:
            neighbors.append((row, 0, (offset[0], offset[1] - 1)))

    return neighbors

def bfs(matrix, start, steps):
    visited = {}

    queue = deque([((start[0], start[1], (0,0)), steps)])
    res = 0
    in_res = set()

    while queue:
        curr, s = queue.popleft()
        row = curr[0]
        col = curr[1]
        offset = curr[2]

        if s == 0:
            if curr not in in_res:
                res += 1
            if curr not in visited:
                visited[curr] = []
            visited[curr].append(s)
            in_res.add(curr)

        elif s > 0:
            if curr not in visited:
                visited[curr] = []

            if s not in visited[curr]:
                visited[curr].append(s)

                for neighbor in check_neighbors(matrix, row, col, ['.', 'S'], offset):
                    queue.append((neighbor, s - 1))
    return len(in_res)


def pt1_solution(lines):
    grid = []
    for x in range(len(lines)):
        line = lines[x].strip()
        grid.append(list(line))
    s = None
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 'S':
                s = (x,y)

    return bfs(grid, s, 64)

def pt2_solution(lines):
    grid = []
    for x in range(len(lines)):
        line = lines[x].strip()
        grid.append(list(line))
    s = None
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 'S':
                s = (x, y)

    half = len(grid) / 2
    fl_half = math.floor(len(grid) / 2)

    # yes I needed some help figuring this next part out :)

    steps = 26501365

    # this is how many grids you can reach in any single direction (up, down, left, right)
    # this is because you can leave the center in a straight line (this wouldn't work if there were obstacles)
    max_sq = (steps - fl_half) / len(grid)

    # you can reach any square in a single grid in one half grid (because you start in the middle)
    single_sq = bfs(grid, s, math.floor(half))

    # you can reach any square in a neighbor (up/down/left/right) in 3 half grids
    neighbor_sq = bfs(grid, s, math.floor(half * 3))

    # you can reach any square in a diagonal neighbor in 5 half grids
    diag_sq = bfs(grid, s, math.floor(half * 5))

    # for every additional grid you add in each direction (total of x grids), you have x^2 diagonal grids
    # so, this is a quadratic equation
    # f(x) = ax^2 + bx + c

    # when max_sq == 1:

    # a (diagonal squares)
    a = diag_sq

    # remove going straight up/down/left/right (you can reach 2 grids by going 5 halves)
    a -= 2 * neighbor_sq

    # account for walking back to the center grid after 5 halves
    a += single_sq

    # divide in 2 because there are two ways to enter each diagonal from the center
    a /= 2

    # b (neighbor squares)

    # there are four overlapping 3x3 grids you can reach in five halves
    b = neighbor_sq * 4

    # remove the inner diagonal grids you reach in five halves
    b -= diag_sq

    # there will be four duplicate sets for walking back to the inner grid of each of the overlapping grids
    # you only need to include one for the true center grid
    b -= 3 * single_sq

    # divide in 2 because the result is for 8 neighbor grids (2 in each direction)
    b /= 2

    # c (inner square)
    c = single_sq

    res = a * math.pow(max_sq, 2) + max_sq * b + c
    return res


if __name__ == '__main__':
    if sys.argv[1] == 't':
        input = open("test.txt", "r")
    else:
        input = open("input.txt", "r")

    lines = input.readlines()

    print("Part 1: " + str(pt1_solution(lines)))
    print("Part 2: " + str(pt2_solution(lines)))