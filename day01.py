"""
cadybaltz
12/01/2023
AoC 2023 Day 1
Part 1: 2103, 00:05:02
Part 2: 3416, 00:31:18
"""

import sys
def find_first_and_last(input):
    number_dict = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    first = ""

    # find the first number
    x = 0
    while x < len(input) and len(first) == 0:
        for word, number in number_dict.items():
            if len(word) > len(input) - x:
                continue
            if input[x:x + len(word)] == word:
                first = number
                break
        if len(first) == 0:
            if input[x].isdigit():
                first = str(input[x])
        x += 1

    # find the last number
    x = len(input) - 1
    while x >= 0:
        if input[x].isdigit():
            return first, input[x]

        for word, number in number_dict.items():
            if len(word) > len(input) - x:
                continue

            if input[x:x + len(word)] == word:
                return first, number
        x -= 1


def solution(file):
    result = 0

    for line in file:
        first, last = find_first_and_last(line)
        result += int(first + last)

    return result


if __name__ == '__main__':
    input = open(sys.argv[1], "r")
    print(solution(input))
