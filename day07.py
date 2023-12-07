"""
cadybaltz
12/07/2023
AoC 2023 Day 7
Part 1: 1517, 00:24:20
Part 2: 3666, 00:59:49
"""

import sys

card_values = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
card_value_map = {value: chr(ord('A') + index) for index, value in enumerate(card_values)}
def solution(file):
    lines = file.readlines()

    ranked = {index: [] for index, _ in enumerate(range(7))}

    bids = {}

    for x in range(len(lines)):
        line = lines[x]

        vals = line.split()
        
        bids[vals[0]] = int(vals[1])
        cards = vals[0]

        joker_ct = 0
        card_ct = {}
        for card in cards:
            if card == 'J':
                joker_ct += 1
            else:
                if card in card_ct:
                    card_ct[card] += 1
                else:
                    card_ct[card] = 1

        if len(card_ct) > 0:
            max_ct = max(card_ct.values(), key=lambda x: x)

        # all jokers
        if len(card_ct) == 0:
            ranked[0].append(vals[0])

        # all 5's
        elif len(card_ct) == 1:
            ranked[0].append(vals[0])

        elif len(card_ct) == 2:
            if max_ct + joker_ct == 4:
                ranked[1].append(vals[0])
            else:
                ranked[2].append(vals[0])

        elif len(card_ct) == 3:
            if joker_ct == 2:
                ranked[3].append(vals[0])
            elif joker_ct == 1:
                ranked[3].append(vals[0])
            else:
                if max_ct == 3:
                    ranked[3].append(vals[0])
                else:
                    ranked[4].append(vals[0])

        elif len(card_ct) == 4:
            ranked[5].append(vals[0])

        elif len(card_ct) == 5:
            ranked[6].append(vals[0])

    max_rank = len(lines)
    total = 0
    for x in range(len(ranked)):

        # convert to alphabetical for easy sorting

        new_list = []
        new_bids = {}
        for s in ranked[x]:
            new_s = ''
            for letter in s:
                new_s = new_s + card_value_map[letter]
            new_list.append(new_s)
            new_bids[new_s] = bids[s]

        ordered = sorted(new_list)
        for val in ordered:
            total += max_rank * new_bids[val]
            max_rank -= 1
    return total


if __name__ == '__main__':
    if sys.argv[1] == 't':
        input = open("test.txt", "r")
    else:
        input = open("input.txt", "r")
    print(solution(input))
