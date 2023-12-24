"""
cadybaltz
12/23/2023
AoC 2023 Day 23
Part 1: 650, 00:20:22
Part 2: 9289, >24h
"""

import sys
from queue import PriorityQueue

def pt_1_rec(grid, curr, end, seen):
    seen.add(curr)

    if curr == end:
        return 0

    elif grid[curr[0]][curr[1]] in slope.keys():
        new_x = curr[0] + slope[grid[curr[0]][curr[1]]][0]
        new_y = curr[1] + slope[grid[curr[0]][curr[1]]][1]
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid_cond(grid, new_x, new_y, seen):
            return 1 + pt_1_rec(grid, (new_x, new_y), end, set(seen))
        else:
            return -10000000000000

    else:
        maxi = -10000000000000000
        neighbors = check_adj(grid, curr[0], curr[1], seen)
        for neighbor in neighbors:
            maxi = max(maxi, pt_1_rec(grid, neighbor, end, seen.copy()))
        return maxi + 1

grid_check = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
]

def grid_cond(grid, x, y, seen):
    if grid[x][y] != '#' and (x,y) not in seen:
        return True
    return False

slope = {
    '>': (0, 1),
    '<': (0, -1),
    '^': (-1,0),
    'v': (1,0)
}
def check_adj(grid, x, y, seen):
    result = []
    for diff in grid_check:
        new_x = x + diff[0]
        new_y = y + diff[1]
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid_cond(grid, new_x, new_y, seen):
            result.append((new_x, new_y))
    return result

def dfs(graph, curr, end, seen):
    priority_queue = PriorityQueue()
    priority_queue.put((0, 0, 1, curr, seen))
    maxi = 0

    while priority_queue.qsize() > 0:
        p, p2, steps, curr, seen = priority_queue.get()

        seen.add(curr)
        if curr == end:
            maxi = max(maxi, steps)

        neighbors = graph[curr]
        for neighbor in neighbors:
            if neighbor[0] not in seen:
                priority_queue.put((-steps, 0, steps + neighbor[1] - 1, neighbor[0], seen.copy()))
    return maxi - 1
def pt_2_pqueue(grid, curr, end, seen):

    old_grid = {}
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] != '#':
                n_map = {}
                neighbors = check_adj(grid, x, y, [])
                for neighbor in neighbors:
                    n_map[neighbor] = 1
                old_grid[(x,y)] = n_map

    condensed_graph = {}

    for node in old_grid.keys():

        neighbors = old_grid[node].keys()

        if len(neighbors) == 2:
            continue

        condensed_graph[node] = []
        for neighbor in neighbors:
            prev = node
            curr = neighbor
            done = False
            chain_len = 1
            while not done:
                chain_len += 1
                next_n = old_grid[curr].keys()
                next_n_k = []
                for key in next_n:
                    if key != prev:
                        next_n_k.append(key)
                if len(next_n_k) == 1:
                    prev = curr
                    curr = next_n_k[0]
                else:
                    done = True
            condensed_graph[node].append((curr, chain_len))
    return dfs(condensed_graph, (0,1), end, set())


def solution(lines, part):
    grid = []

    for x in range(len(lines)):
        line = lines[x].strip()
        grid.append(list(line))

    if part == 1:
        return pt_1_rec(grid, (0,1), (len(grid)-1, len(grid[0])-2), set())
    else:
        return pt_2_pqueue(grid, (0, 1), (len(grid) - 1, len(grid[0]) - 2), set())


if __name__ == '__main__':
    if sys.argv[1] == 't':
        input = open("test.txt", "r")
    else:
        input = open("input.txt", "r")

    lines = input.readlines()
    sys.setrecursionlimit(10000)

    print("Part 1: " + str(solution(lines, 1)))
    print("Part 2 started - takes around 2 min")
    print("Part 2: " + str(solution(lines, 2)))


