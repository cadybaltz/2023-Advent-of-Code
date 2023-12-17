"""
cadybaltz
12/17/2023
AoC 2023 Day 17
Part 1: 13371, 16:57:37
Part 2: 12869, 18:26:12
"""

import sys
import heapq

turn = {
    'N': ['E', 'W'],
    'E': ['N', 'S'],
    'S': ['E', 'W'],
    'W': ['N', 'S']
}

move = {
    'N': (-1, 0),
    'E': (0, 1),
    'S': (1, 0),
    'W': (0, -1)
}

def possible_moves(dir, cumu, part):
    if part == 1:
        
        # can only go straight up to 3 times in a row
        if cumu < 2:
            return turn[dir] + [dir]
        
        else:
            return turn[dir]

    elif part == 2:
        
        # must go straight if you have not moved in the same direction 4 times in a row
        if cumu < 3:
            return [dir]
        
        # can only go straight up to 10 times in a row
        elif cumu < 9:
            return turn[dir] + [dir]
        else:
            return turn[dir]


def next_moves(curr, dir, cumu, grid, part):
    valid_moves = []
    for direction in possible_moves(dir, cumu, part):
        change = move[direction]
        next_node = (curr[0] + change[0], curr[1] + change[1])
        if 0 <= next_node[0] < len(grid) and 0 <= next_node[1] < len(grid[0]):
            valid_moves.append((next_node, direction))

    return valid_moves

def solution(lines, part):
    grid = []
    for line in lines:
        grid.append([int(char) for char in line.strip()])

    start = (0, 0)
    end = (len(grid) - 1, len(grid[0]) - 1)

    # can start by going east or west
    pqueue = [(0, start, 'E', -1), (0, start, 'S', -1)]
    visited = set()

    while pqueue:
        cost, curr, dir, cumu = heapq.heappop(pqueue)

        # for part 2, must have moved straight at least 4 times in a row before reaching end
        if curr == end and ((part == 2 and cumu >= 3) or part == 1):
            return cost

        if (curr, dir, cumu) in visited:
            continue
        visited.add((curr, dir, cumu))

        for new_pos, new_dir in next_moves(curr, dir, cumu, grid, part):
            new_cost = cost + grid[new_pos[0]][new_pos[1]]
            new_cumu = (cumu + 1) if dir == new_dir else 0
            heapq.heappush(pqueue, (new_cost, new_pos, new_dir, new_cumu))

if __name__ == '__main__':
    if sys.argv[1] == 't':
        input = open("test.txt", "r")
    else:
        input = open("input.txt", "r")
    lines = input.readlines()

    print("Part 1: " + str(solution(lines, 1)))
    print("Part 2: " + str(solution(lines, 2)))
