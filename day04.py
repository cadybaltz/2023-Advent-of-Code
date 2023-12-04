"""
cadybaltz
12/04/2023
AoC 2023 Day 4
Part 1: 171, 00:03:15
Part 2: 344, 00:09:56
"""

import sys


def solution(file):
    lines = file.readlines()
    pt1_total = 0

    copies = {}
    card = 1

    # initialize all copies to 1
    for x in range(len(lines)):
        copies[x + 1] = 1

    for line in lines:
        colon = line.split(':')
        hands = colon[1].split('|')
        winners = hands[0].split()
        yours = hands[1].split()

        points = 0
        matches = 0
        for num in yours:
            if num in winners:
                if points == 0:
                    points = 1
                else:
                    points = points * 2
                matches += 1

        for x in range(copies[card]):
            for y in range(matches):
                # makes copies of the following cards based on number of matches in this round
                copies[card + 1 + y] += 1

        pt1_total += points
        card += 1

    pt2_total = 0
    for x in copies.values():
        pt2_total += x

    return pt1_total, pt2_total


if __name__ == '__main__':
    if sys.argv[1] == 't':
        input = open("test.txt", "r")
    else:
        input = open("input.txt", "r")
    print(solution(input))
