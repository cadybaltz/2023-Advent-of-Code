"""
cadybaltz
12/13/2023
AoC 2023 Day 13
Part 1: 1853, 00:27:11
Part 2: 890, 00:28:41
"""
import sys

def has_vert(graph, part):
    for x in range(0, len(graph[0])):
        diff = 0
        same = True
        iter = False
        for y in range(0, len(graph)):
            if x - y >= 0 and x + y + 1 < len(graph[0]):
                for z in range(len(graph)):
                    
                    iter = True
                    if graph[z][x - y] != graph[z][x + y + 1]:
                        diff += 1
                        same = False
        if part == 2 and diff == 1:
            return x
        elif part == 1 and same and iter:
            return x
    return None

def has_hor(graph, part):
    for x in range(0, len(graph)):
        diff = 0
        same = True
        iter = False
        for y in range(0, len(graph)):
            if x-y >= 0 and x+y+1 < len(graph):
                for z in range(len(graph[0])):
                    iter = True
                    if graph[x - y][z] != graph[x + y + 1][z]:
                        diff += 1
                        same = False
        if part == 2 and diff == 1:
            return x
        elif part == 1 and same and iter:
            return x
    return None
            

def solution(lines, part):
    result = 0
    patterns = []
    curr = []

    for x in range(len(lines)):
        line = lines[x].strip()
        if len(line) == 0:
            patterns.append(curr)
            curr = []
        else:
            curr.append(line)
    patterns.append(curr)
    
    for pattern in patterns:
        vert = has_vert(pattern, part)
        hor = has_hor(pattern, part)
        if vert is not None:
            result += vert + 1
        else:
            result += (hor + 1) * 100
    
    return result

if __name__ == '__main__':
    if sys.argv[1] == 't':
        input = open("test.txt", "r")
    else:
        input = open("input.txt", "r")
        
    lines = input.readlines()
    print("Part 1: " + str(solution(lines, 1)))
    print("Part 2: " + str(solution(lines, 2)))