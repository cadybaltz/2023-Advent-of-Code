"""
cadybaltz
12/11/2023
AoC 2023 Day 11
Part 1: 1937, 00:19:18
Part 2: 5091, 00:58:52
"""
import sys

def solution(file, expansion_value):
    lines = file.readlines()
    result = 0

    original = []

    for x in range(len(lines)):
        line = lines[x].strip()
        original.append([val for val in line])

    galaxies = [(x, y) for x in range(len(original)) for y in range(len(original[0])) if original[x][y] == '#']

    # check all the rows
    expanded = []
    for x in range(len(original)):
        has_galaxy = False
        for y in range(len(original[0])):
            if original[x][y] == '#':
                has_galaxy = True
        if not has_galaxy:
            expanded.append(['e' for _ in range(len(original[x]))])
        else:
            expanded.append(original[x])

    # check all the columns
    for y in range(len(expanded[0])):
        has_g = False
        for x in range(len(expanded)):
            if expanded[x][y] == '#':
                has_g = True
        if not has_g:
            for x in range(len(expanded)):
                expanded[x][y] = 'e'

    for x in range(len(galaxies)):
        for y in range(x + 1, len(galaxies)):
            first = galaxies[x]
            second = galaxies[y]

            higher_x = max(first[0], second[0])
            higher_y = max(first[1], second[1])

            lower_x = min(first[0], second[0])
            lower_y = min(first[1], second[1])

            while lower_x < higher_x:
                result += expansion_value if expanded[lower_x][lower_y] == 'e' else 1
                lower_x += 1

            while lower_y < higher_y:
                result += expansion_value if expanded[lower_x][lower_y] == 'e' else 1
                lower_y += 1

    return result


if __name__ == '__main__':
    # Part 1
    if sys.argv[1] == 't':
        input = open("test.txt", "r")
    else:
        input = open("input.txt", "r")
    print(solution(input, 2))

    # Part 2
    if sys.argv[1] == 't':
        input = open("test.txt", "r")
    else:
        input = open("input.txt", "r")
    print(solution(input, 1000000))
