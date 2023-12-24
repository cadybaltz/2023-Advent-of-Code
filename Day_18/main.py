"""
cadybaltz
12/16/2023
AoC 2023 Day 16
Part 1: 849, 00:22:15
Part 2: 666, 00:26:26
"""

import sys

def pretty_print_grid(grid):
    with open("output3.txt", 'w') as file:
        for row in grid:
            file.write(''.join(row) + '\n')

dir = {
    'R': (0,1),
    'L': (0,-1),
    'U': (-1,0),
    'D': (1,0)
}

def get_neighbors(grid, row, col):
    neighbors = []
    num_rows, num_cols = len(grid), len(grid[0])

    # Check top neighbor
    if row > 0:
        neighbors.append(grid[row - 1][col])

    # Check bottom neighbor
    if row < num_rows - 1:
        neighbors.append(grid[row + 1][col])

    # Check left neighbor
    if col > 0:
        neighbors.append(grid[row][col - 1])

    # Check right neighbor
    if col < num_cols - 1:
        neighbors.append(grid[row][col + 1])

    return neighbors

def solution(lines):
    result = 0

    grid = []
    for x in range(2000):
        grid.append(['.'] * 2000)

    grid[1000][1000] = "#"
    curr = (1000,1000)
    r = 0
    l = 0
    u = 0
    d = 0

    min_x = 2000
    max_x = 0
    min_y = 2000
    max_y = 0

    for x in range(len(lines)):
        line = lines[x].strip()
        info = line.split()

        change = dir[info[0]]
        if info[0] == 'L':
            l += int(info[1])
        elif info[0] == 'U':
            u += int(info[1])
        elif info[0] == 'D':
            d += int(info[1])
        elif info[0] == 'R':
            r += int(info[1])

        c = 0
        while c < int(info[1]):
            curr = (curr[0] + change[0], curr[1] + change[1])
            min_x = min(min_x, curr[0])
            max_x = max(max_x, curr[0])

            min_y = min(min_y, curr[1])
            max_y = max(max_y, curr[1])

            #if 0 <= curr[0] and curr[0] < len(grid) and 0 <= curr[1] and curr[1] < len(grid[0]):

            if grid[curr[0]][curr[1]] == "#":
                print("HELP")
            grid[curr[0]][curr[1]] = "#"
            c += 1

    for y in range(len(grid[0])):
        x = 0
        while x < len(grid) and (grid[x][y] == '.' or grid[x][y] == 'x'):
            grid[x][y] = 'x'
            x += 1
        x = len(grid) - 1
        while x >= 0 and (grid[x][y] == '.' or grid[x][y] == 'x'):
            grid[x][y] = 'x'
            x -= 1

    # 251, 253, 1171, 80276, 80275, 83749

    for x in range(len(grid)):
        y = 0
        while y < len(grid[0]) and (grid[x][y] == '.' or grid[x][y] == 'x'):
            grid[x][y] = 'x'
            y += 1

        y = len(grid[0]) - 1
        while y >= 0 and (grid[x][y] == '.' or grid[x][y] == 'x'):
            grid[x][y] = 'x'
            y -= 1

    changed = True
    while changed:
        changed = False
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '.':
                    neighbors = get_neighbors(grid, x, y)
                    for neighbor in neighbors:
                        if neighbor == 'x':
                            grid[x][y] = 'x'
                            changed = True

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == '#' or grid[x][y] == '.':
                result += 1

    width = max_x - min_x
    height = max_y - min_y
    print(width)
    print(height)

    # perim = (height + 1) * 2 + (width - 2) * 2
    # perim2 = (l + 1) * 2 + (d - 2) * 2

    print(d)
    print(l)
    # print(perim)
    # print(perim2)

    # max
    print(((width + 1) * (height + 1)))

    # actual
    print(d * l)

    print(2 * abs(d - (width + 1)))
    print(2 * abs(l - (height + 1)))

    return (2 * abs(d - (width + 1))) + (2 * abs(l - (height + 1)))


if __name__ == '__main__':
    if sys.argv[1] == 't':
        input = open("test.txt", "r")
    else:
        input = open("input.txt", "r")

    lines = input.readlines()

    print(solution(lines))
