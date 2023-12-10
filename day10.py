"""
cadybaltz
12/10/2023
AoC 2023 Day 10
Part 1: 6856, 01:40:43
Part 2: 5940, 04:27:22
"""
import copy
import sys

# 674, 803, 995, 6815

start = None
def is_squeeze_up(x, y, graph):
    if y + 1 >= len(graph[0]):
        return False

    up = {
        'J': ['L', 'F', '|'],
        '7': ['F', '|', 'L'],
        '|': ['L', 'F', '|']
    }

    if graph[x][y] in up and graph[x][y + 1] in up[graph[x][y]]:
        return True
    return False


def is_squeeze_side(x, y, graph):
    if x + 1 >= len(graph):
        return False

    side = {
        'J': ['7', 'F', '-'],
        'L': ['F', '-', '7'],
        '-': ['7', 'F', '-']
    }

    if graph[x][y] in side and graph[x + 1][y] in side[graph[x][y]]:
        return True
    return False


def update_helper(count, coords, graph, distances):
    if count < distances[coords[0]][coords[1]]:
        update(count, coords, graph, distances)

def update(count, coords, graph, distances):

    if graph[coords[0]][coords[1]] == '.':
        return

    distances[coords[0]][coords[1]] = min(count, distances[coords[0]][coords[1]])

    curr = graph[coords[0]][coords[1]]

    move = {
        '|': [(1, 0), (-1, 0)],
        '-': [(0, 1), (0, -1)],
        'L': [(0, 1), (-1, 0)],
        'J': [(-1, 0), (0, -1)],
        '7': [(1, 0), (0, -1)],
        'F': [(1, 0), (0, 1)]
    }

    for sym, moves in move.items():
        if curr == sym:
            for move in moves:
                update_helper(count + 1, (coords[0] + move[0], coords[1] + move[1]), graph, distances)

    if curr == 'S':
        # left
        if coords[1] > 0:
            if graph[coords[0]][coords[1] - 1] in ['-', 'L', 'F']:
                update_helper(count + 1, (coords[0], coords[1] - 1), graph, distances)

        # right
        if coords[1] < len(graph[0]) - 1:
            if graph[coords[0]][coords[1] + 1] in ['-', 'J', '7']:
                update_helper(count + 1, (coords[0], coords[1] + 1), graph, distances)

        # up
        if coords[0] > 0:
            if graph[coords[0] - 1][coords[1]] in ['|', '7', 'F']:
                update_helper(count + 1, (coords[0] - 1, coords[1]), graph, distances)

        # down
        if coords[0] < len(graph) - 1:
            if graph[coords[0] + 1][coords[1]] in ['|', 'J', 'L']:
                update_helper(count + 1, (coords[0] + 1, coords[1]), graph, distances)

    return None


def solution(file):

    lines = file.readlines()

    start_coords = None
    graph = []
    distances = []

    for x in range(len(lines)):
        line = lines[x].strip()
        r = []
        r_n = []
        for val in line:
            r.append(val)
            r_n.append(sys.maxsize)
        graph.append(r)
        distances.append(r_n)

    # PART 1:

    for x in range(len(graph)):
        for y in range(len(graph[0])):
            if graph[x][y] == 'S':
                start_coords = (x, y)
    update(0, start_coords, graph, distances)

    maxi = 0
    for x in distances:
        for y in x:
            if y != sys.maxsize:
                maxi = max(y, maxi)

    # PART 2:

    pt_2_graph = []
    for x in range(len(distances)):
        row = []
        for y in range(len(distances[0])):
            # any location not part of the main loop should be considered
            if distances[x][y] == sys.maxsize:
                row.append(0)
            else:
                row.append(graph[x][y])
        pt_2_graph.append(row)

    # first expand horizontally
    hori_expand = []
    for x in range(len(pt_2_graph)):
        row = []
        for y in range(len(pt_2_graph[0])):
            if pt_2_graph[x][y] == 0:
                # only keep one 0 to remember how many spots were in the original
                row.append(0)
                row.append(-1)
            elif is_squeeze_up(x, y, pt_2_graph):
                # add empty space for parallel
                row.append(pt_2_graph[x][y])
                row.append(-1)
            else:
                row.append(pt_2_graph[x][y])
                row.append(pt_2_graph[x][y])
        hori_expand.append(row)

    # now expand vertically too
    expand = []
    for x in range(len(hori_expand)):
        row = []
        new_row = []
        for y in range(len(hori_expand[0])):
            if hori_expand[x][y] == 0 or hori_expand[x][y] == -1:
                row.append(hori_expand[x][y])
                new_row.append(-1)
            elif is_squeeze_side(x, y, hori_expand):
                # add empty space for parallel
                row.append(1)
                new_row.append(-1)
            else:
                row.append(1)
                new_row.append(1)
        expand.append(row)
        expand.append(new_row)

    # start spreading the number 2 from the edges
    for x in range(len(expand)):

        # left to right
        y = 0
        while y < len(expand[0]):
            if expand[x][y] == 1:
                break
            else:
                expand[x][y] = 2
            y += 1

        # right to left
        y = len(expand[0]) - 1
        while y >= 0:
            if expand[x][y] == 1:
                break
            else:
                expand[x][y] = 2
            y -= 1

    # keep spreading 2 until there are no more changes to make
    changed_last_iter = True
    while changed_last_iter:
        changed_last_iter = False

        for x in range(len(expand)):
            for y in range(len(expand[0])):
                if expand[x][y] == 2:
                    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
                    neighbors = [(x + r, y + c) for r, c in directions if
                                 0 <= x + r < len(expand) and 0 <= y + c < len(expand[0])]
                    for neighbor in neighbors:
                        if expand[neighbor[0]][neighbor[1]] == 0 or expand[neighbor[0]][neighbor[1]] == -1:
                            changed_last_iter = True
                            expand[neighbor[0]][neighbor[1]] = 2

    # count all of the original spaces that were not changed to 2
    total = 0
    for x in range(len(expand)):
        for y in range(len(expand[0])):
            if expand[x][y] == 0:
                total += 1

    return maxi, total


if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    if sys.argv[1] == 't':
        input = open("test.txt", "r")
    else:
        input = open("input.txt", "r")
    print(solution(input))
