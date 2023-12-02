"""
cadybaltz
12/02/2023
AoC 2023 Day 2
Part 1: 1081, 00:09:21
Part 2: 1090, 00:13:02
"""

import sys
import re

def solution(file):
    lines = file.readlines()

    result = 0

    for line_num in range(len(lines)):
        line = lines[line_num]

        rounds = line.split(';')

        red = 12
        green = 13
        blue = 14

        possible = True

        min_r = 0
        min_g = 0
        min_b = 0

        for round in rounds:
            pattern = re.compile(r'(\d+) red|(\d+) green|(\d+) blue')
            matches = pattern.findall(round)

            green_sum = 0
            red_sum = 0
            blue_sum = 0

            for match in matches:
                red_sum += int(match[0]) if match[0] else 0
                green_sum += int(match[1]) if match[1] else 0
                blue_sum += int(match[2]) if match[2] else 0

            # part 1 logic
            if green_sum > green or blue_sum > blue or red_sum > red:
                possible = False

            # part 2 logic
            min_r = max(red_sum, min_r)
            min_g = max(green_sum, min_g)
            min_b = max(blue_sum, min_b)

        # part 1 calculation
        # if possible:
        #     result += line_num + 1

        # part 2 calculation
        result += min_r * min_g * min_b

    return result


if __name__ == '__main__':
    if sys.argv[1] == 't':
        input = open("test.txt", "r")
    else:
        input = open("input.txt", "r")
    print(solution(input))
