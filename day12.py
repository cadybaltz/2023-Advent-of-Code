"""
cadybaltz
12/12/2023
AoC 2023 Day 12
Part 1: 1785, 00:29:15
Part 2: 18566, >24h
"""
import sys

memo = {}

def memo_and_return(cache_key, result):
    memo[cache_key] = result
    return result

def count_rec(plan, keys):
    # convert input into hashable key
    cache_key = plan + '/'
    for key in keys:
        cache_key += key + ','

    if cache_key in memo:
        return memo[cache_key]

    if len(plan) == 0:
        if len(keys) == 0:
            return memo_and_return(cache_key, 1)
        else:
            return memo_and_return(cache_key, 0)
        
    if plan[0] == '#':
        count = 0
        x = 0
        if len(keys) == 0:
            return memo_and_return(cache_key, 0)
        
        while x < len(plan) and (plan[x] == '#' or (plan[x] == '?' and count < int(keys[0]))):
            count += 1
            x += 1

            if x == len(plan):
                if count < int(keys[0]):
                    return memo_and_return(cache_key, 0)

        # need a '.' before the next key can start
        if x < len(plan) and plan[x] == '?':
            x += 1

        if count != int(keys[0]):
            return memo_and_return(cache_key, 0)
        else:
            return memo_and_return(cache_key, count_rec(plan[x:], keys[1:]))
        
    elif plan[0] == '?':
        return memo_and_return(cache_key, count_rec('#' + plan[1:], keys) + count_rec('.' + plan[1:], keys))
    
    else:
        x = 0
        while x < len(plan) and plan[x] == '.':
            x += 1
        return memo_and_return(plan[x:], count_rec(plan[x:], keys))


if __name__ == '__main__':
    if sys.argv[1] == 't':
        input = open("test.txt", "r")
    else:
        input = open("input.txt", "r")
    lines = input.readlines()

    pt1_total = 0
    pt2_total = 0
    for x in range(len(lines)):
        memo = {}
        line = lines[x].strip()
        values = line.split()
        plan = values[0].strip()
        key = values[1].strip()
        keys = key.split(',')
        pt1_total += count_rec(plan, keys)
        pt2_total += count_rec((plan + '?') * 4 + plan, keys * 5)
    print("Part 1: " + str(pt1_total))
    print("Part 2: " + str(pt2_total))