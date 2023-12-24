"""
cadybaltz
12/24/2023
AoC 2023 Day 24
Part 1: 5376, 05:00:54
Part 2: 5621, 17:56:08
"""

import sys
from z3 import *

def slope_yint(x, y, vx, vy):
    m = vy / vx
    b = y - m * x
    return m, b

def int_times(m1, b1, m2, b2):
    if m1 == m2:
        return None

    int = (b2 - b1) / (m1 - m2)
    if int >= 0:
        return int
    else:
        return None

def pt1_solution(lines):
    result = 0

    positions = []
    velocities = []

    for x in range(len(lines)):
        line = lines[x].strip()
        pos = line.split('@')[0].split(', ')
        vel = line.split('@')[1].split(', ')
        pos = [int(val.strip()) for val in pos]
        vel = [int(val.strip()) for val in vel]
        positions.append(pos)
        velocities.append(vel)

    mini = 200000000000000
    maxi = 400000000000000

    # wrong: 21148, 19938

    for x in range(len(positions)):
        for y in range(x, len(positions)):
            if x != y:

                m1, b1 = slope_yint(positions[x][0], positions[x][1], velocities[x][0], velocities[x][1])
                m2, b2 = slope_yint(positions[y][0], positions[y][1], velocities[y][0], velocities[y][1])
                time = int_times(m1, b1, m2, b2)

                if time is not None:
                    is_valid = True
                    for val in [time, m1 * time + b1, m2 * time + b2]:
                        if not (mini <= val <= maxi):
                            is_valid = False
                    if is_valid:
                        t1 = (time - positions[x][0]) / velocities[x][0]
                        t2 = (time - positions[y][0]) / velocities[y][0]
                        if t1 > 0 and t2 > 0:
                            result += 1

    return result

def pt2_solution(lines):
    positions = []
    velocities = []

    for line in lines:
        pos, vel = line.split('@')
        pos = [int(val.strip()) for val in pos.split(',')]
        vel = [int(val.strip()) for val in vel.split(',')]
        positions.append(pos)
        velocities.append(vel)

    x0, y0, z0, vx, vy, vz = Reals('x0 y0 z0 vx vy vz')

    # each time of intersection is an unknown
    times = [Real(f'{i}') for i in range(len(positions))]
    solver = Solver()

    # ensure position is equal for each input
    for i in range(len(positions)):
        eq_x = x0 + vx * times[i] == positions[i][0] + velocities[i][0] * times[i]
        eq_y = y0 + vy * times[i] == positions[i][1] + velocities[i][1] * times[i]
        eq_z = z0 + vz * times[i] == positions[i][2] + velocities[i][2] * times[i]
        solver.add(eq_x, eq_y, eq_z)
        
    # ensure time is positive
    for i in range(len(times)):
        solver.add(times[i] > 0)

    if solver.check() == sat:
        model = solver.model()
        return model[x0], model[y0], model[z0]


if __name__ == '__main__':
    if sys.argv[1] == 't':
        input = open("test.txt", "r")
    else:
        input = open("input.txt", "r")

    lines = input.readlines()
    print("Part 1: " + str(pt1_solution(lines)))
    print("Part 2: " + str(pt2_solution(lines)))

