"""
cadybaltz
12/25/2023
AoC 2023 Day 25
Part 1: 2915, 02:40:22
Part 2: 2447, 02:40:26
Merry Christmas to all, and to all a good night
"""
import random
import sys

def get_cut_cost(n, group, wires):
    cost = 0
    for neighbor in wires[n]:
        if neighbor in group:
            cost += wires[n][neighbor]
    return cost
def solution(lines):
    neighbors = {}
    nodes = []
    edges = []

    for x in range(len(lines)):
        line = lines[x].strip()
        first = line.split(":")[0]
        rest = line.split(":")[1].split()

        for n in rest:
            if n not in neighbors:
                neighbors[n] = set()
            if first not in neighbors:
                neighbors[first] = set()
            neighbors[n].add(first)
            neighbors[first].add(n)

            if first not in nodes:
                nodes.append(first)
            if n not in nodes:
                nodes.append(n)
            edges.append((first, n))

    # run Karger's algorithm
    while True:
        curr_edges = edges.copy()
        curr_nodes = {}
        for node in nodes:
            curr_nodes[node] = [node]

        while len(curr_nodes) > 2:
            # randomly contract an edge until you have condensed into two nodes
            edge_to_contract = random.choice(curr_edges)
            curr_edges.remove(edge_to_contract)

            first = edge_to_contract[0]
            second = edge_to_contract[1]

            new_curr_edges = []
            for edge in curr_edges:
                # merge edges from the second node into the first
                if edge[0] == second:
                    if first != edge[1]:
                        new_curr_edges.append((first, edge[1]))
                elif edge[1] == second:
                    if edge[0] != first:
                        new_curr_edges.append((edge[0], first))
                else:
                    new_curr_edges.append(edge)
            curr_edges = new_curr_edges

            # keep track of how any nodes have been merged into one
            curr_nodes[first] = curr_nodes[first] + curr_nodes[second]

            del curr_nodes[second]

        result = list(curr_nodes.values())
        edge_count = 0

        # count how many edges go between the two sets
        for x in range(len(result[0])):
            for y in range(len(result[1])):
                if result[1][y] in neighbors[result[0][x]]:
                    edge_count += 1

        # if you have found a division with only three edges in between, multiply the sizes of each set
        if edge_count == 3:
            return len(result[0]) * len(result[1])

if __name__ == '__main__':
    if sys.argv[1] == 't':
        input = open("test.txt", "r")
    else:
        input = open("input.txt", "r")

    lines = input.readlines()
    print(solution(lines))

