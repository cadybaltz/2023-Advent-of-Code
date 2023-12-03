"""
cadybaltz
12/03/2023
AoC 2023 Day 3
Part 1: 1229, 00:18:22
Part 2: 2898, 00:44:40
"""

import sys

grid_check = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1)
]


def grid_cond_pt_1(grid, x, y):
    return grid[x][y] != '.' and not grid[x][y].isdigit()


def grid_cond_pt_2(grid, x, y):
    return grid[x][y] == '*'


def check_adj_pt_1(grid, x, y):
    for diff in grid_check:
        new_x = x + diff[0]
        new_y = y + diff[1]
        if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid) and grid_cond_pt_1(grid, new_x, new_y):
            return True

    return False


def check_adj_pt_2(grid, x, y):
    result = []

    for diff in grid_check:
        new_x = x + diff[0]
        new_y = y + diff[1]
        if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid) and grid_cond_pt_2(grid, new_x, new_y):
            result.append((new_x, new_y))

    return result


def solution(file):
    lines = file.readlines()

    # store input as grid matrix
    grid = []
    for line_num in range(len(lines)):
        line = lines[line_num]
        row = []
        for ch in line.strip():
            row.append(ch)
        grid.append(row)

    # pt1_sum = 0

    gears = {}

    for r in range(len(grid)):
        row = grid[r]

        c = 0
        while c < len(row):
            if row[c].isdigit():

                # part 1 logic
                # is_part = check_adj_pt_1(grid, r, c)

                stars = check_adj_pt_2(grid, r, c)

                digit = row[c]
                c += 1
                while c < len(row) and row[c].isdigit():

                    # part 1 logic
                    # if not is_part and check_adj_pt_1(grid, r, c):
                    #     is_part = True

                    for val in check_adj_pt_2(grid, r, c):
                        stars.append(val)

                    digit = digit + row[c]
                    c += 1

                # Part 1 Calulation
                # if is_part:
                #     pt1_sum += int(digit)

                seen = []
                for star in stars:
                    gear_key = str(star[0]) + ',' + str(star[1])
                    if gear_key in gears:

                        # avoid counting the same gear twice for the same number
                        if gear_key not in seen:
                            gears[gear_key].append(int(digit))

                    else:
                        gears[gear_key] = [int(digit)]

                    seen.append(gear_key)

            else:
                c += 1

    # return pt1_sum

    pt2_sum = 0
    for k in gears:
        if len(gears[k]) == 2:
            pt2_sum += gears[k][0] * gears[k][1]
    return pt2_sum


if __name__ == '__main__':
    if sys.argv[1] == 't':
        input = open("test.txt", "r")
    else:
        input = open("input.txt", "r")
    print(solution(input))
