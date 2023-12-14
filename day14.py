"""
cadybaltz
12/14/2023
AoC 2023 Day 14
Part 1: 530, 00:07:02
Part 2: 73, 00:15:43
"""

import sys

def solution(lines, part):
    g = []
    result = 0
    seen = {}
    cycle = None

    for x in range(len(lines)):
        line = lines[x].strip()
        g.append(list(line))

    if part == 1:
        # north
        for x in range(1, len(g)):
            for y in range(len(g[0])):
                if g[x][y] == 'O':
                    z = x - 1
                    while z >= 0 and g[z][y] == '.':
                        z -= 1
                    g[x][y] = '.'
                    g[z + 1][y] = 'O'
        result = 0
        for x in range(len(g)):
            for y in range(len(g[0])):
                if g[x][y] == 'O':
                    result += len(g) - x
        return result

    elif part == 2:
        count = 0
        while cycle is None:
            # north
            for x in range(1, len(g)):
                for y in range(len(g[0])):
                    if g[x][y] == 'O':
                        z = x - 1
                        while z >= 0 and g[z][y] == '.':
                            z -= 1
                        g[x][y] = '.'
                        g[z+1][y] = 'O'

            # west
            for y in range(1, len(g[0])):
                for x in range(len(g)):
                    if g[x][y] == 'O':
                        z = y - 1
                        while z >= 0 and g[x][z] == '.':
                            z -= 1
                        g[x][y] = '.'
                        g[x][z + 1] = 'O'

            # south
            for x in range(len(g)-1,-1,-1):
                for y in range(len(g[0])):
                    if g[x][y] == 'O':
                        z = x + 1
                        while z < len(g) and g[z][y] == '.':
                            z += 1
                        g[x][y] = '.'
                        g[z - 1][y] = 'O'

            # east
            for y in range(len(g[0])-1,-1,-1):
                for x in range(len(g)):
                    if g[x][y] == 'O':
                        z = y + 1
                        while z < len(g[0]) and g[x][z] == '.':
                            z += 1
                        g[x][y] = '.'
                        g[x][z - 1] = 'O'

            result = 0

            for x in range(len(g)):
                for y in range(len(g[0])):
                    if g[x][y] == 'O':
                        result += len(g) - x
            if result in seen:
                cycle = count - seen[result]
            else:
                seen[result] = count
            count += 1

        # seen[result] = start of first cycle
        # cycle = cycle length
        for a in range((1000000000 - seen[result]) % cycle):
            # north
            for x in range(1, len(g)):
                for y in range(len(g[0])):
                    if g[x][y] == 'O':
                        z = x - 1
                        while z >= 0 and g[z][y] == '.':
                            z -= 1
                        g[x][y] = '.'
                        g[z+1][y] = 'O'

            # west
            for y in range(1, len(g[0])):
                for x in range(len(g)):
                    if g[x][y] == 'O':
                        z = y - 1
                        while z >= 0 and g[x][z] == '.':
                            z -= 1
                        g[x][y] = '.'
                        g[x][z + 1] = 'O'

            # south
            for x in range(len(g)-1,-1,-1):
                for y in range(len(g[0])):
                    if g[x][y] == 'O':
                        z = x + 1
                        while z < len(g) and g[z][y] == '.':
                            z += 1
                        g[x][y] = '.'
                        g[z - 1][y] = 'O'

            # east
            for y in range(len(g[0])-1,-1,-1):
                for x in range(len(g)):
                    if g[x][y] == 'O':
                        z = y + 1
                        while z < len(g[0]) and g[x][z] == '.':
                            z += 1
                        g[x][y] = '.'
                        g[x][z - 1] = 'O'

        result = 0
        for x in range(len(g)):
            for y in range(len(g[0])):
                if g[x][y] == 'O':
                    result += len(g) - x
        return result


if __name__ == '__main__':
    if sys.argv[1] == 't':
        input = open("test.txt", "r")
    else:
        input = open("input.txt", "r")

    lines = input.readlines()
    print("Part 1: " + str(solution(lines, 1)))
    print("Part 2: " + str(solution(lines, 2)))