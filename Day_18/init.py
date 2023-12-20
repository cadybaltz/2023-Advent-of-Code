"""
cadybaltz
11/30/2023
Python program to download the user's input from the AoC site to a file called input.txt
    *
   ***
  *****
 *******
*********
    |
"""

import requests
import os

if __name__ == '__main__':

    # place this script in a directory with the format "Day_xx"
    current_directory = os.path.dirname(os.path.abspath(__file__))
    day = int(current_directory[len(current_directory)-2:])

    # the user's session_id should be in a file called key
    with open("../key", 'r') as file:
        session_id = file.read()

    response = requests.get(url="https://adventofcode.com/2023/day/" + str(day) + "/input", cookies={"session": session_id})

    with open("input.txt", 'w') as file:
        file.write(response.text)