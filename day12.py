"""
cadybaltz
12/12/2023
AoC 2023 Day 12
Part 1: 1937, 00:19:18
Part 2: 5091, 00:58:52
"""
import sys
from itertools import product
from queue import Queue



def generate_permutations_with_repetition(patterns, length):
    permutations_list = list(product(patterns, repeat=length))

    filtered_permutations = [perm for perm in permutations_list if 'hh' not in ''.join(perm)]

    return filtered_permutations

def generate_permutations_with_zeros_ones(num_zeros, num_ones):
    total_bits = num_zeros + num_ones
    total_combinations = 1 << total_bits

    combinations = []

    for i in range(total_combinations):
        binary_representation = bin(i)[2:].zfill(total_bits)
        current_combination = [int(bit) for bit in binary_representation]

        if current_combination.count(0) == num_zeros and current_combination.count(1) == num_ones:
            combinations.append(current_combination)

    return combinations

def is_valid(input, keys):
    x = 0
    key = 0
    while x < len(input):
        while x < len(input) and input[x] != '#':
            x += 1
        count = 0
        
        while x < len(input) and input[x] == '#':
            count += 1
            x += 1
        if key >= len(keys):
            while x < len(input):
                if input[x] == '#':
                    return False
                x+=1
            return True
        if key >= len(keys) or count != int(keys[key]):
            return False
        key += 1
        x += 1
    return True

#
# def prune(option, val, keys, opt_set, h):
#
#     result = is_valid(option[0] + val, keys * (h + 2)) and (option[0] + val) not in opt_set
#     opt_set.add((option[0] + val))
#     return result
#
#
# def helper(lines, enter):
#
#     all = []
#
#     result = 0
#     starth = 0
#     startd = 0
#     endinh = 0
#     endind = 0
#     r= []
#
#     poss = ['#', '.']
#     #print(list(product(poss, repeat=5)))
#
#     for x in range(len(lines)):
#         # print(x)
#         line = lines[x]
#         # print(line)
#
#
#
#         plan = line[0]
#         key = line[1]
#
#         plan = '?'.join([plan] * enter)
#         #print(plan)
#         keys = key.split(',')
#         keys = keys * enter
#         #print(keys)
#
#         q = []
#         hc = 0
#         for y in range(len(plan)):
#             if plan[y] == '?':
#                 q.append(y)
#             elif plan[y] == '#':
#                 hc += 1
#
#         t = 0
#         for a in keys:
#             t += int(a)
#
#         possible_orders = generate_permutations_with_zeros_ones(t - hc, len(q) - (t - hc))
#
#         new_poss = []
#         for f in possible_orders:
#             ppp = ""
#             for l in f:
#                 if l == 0:
#                     ppp += '#'
#                 else:
#                     ppp += '.'
#             new_poss.append(ppp)
#
#         # print("after")
#         # new_poss = []
#         # for order in possible_orders:
#         #     s = 0
#         #     for d in order:
#         #         if d == '#':
#         #             s += 1
#         #     if (s + hc) == t:
#         #         new_poss.append(order)
#
#         ths= 0
#         for z in range(len(new_poss)):
#             test = ""
#             p = 0
#             for y in range(len(plan)):
#                 if plan[y] == '?':
#                     test = test + new_poss[z][p]
#                     p += 1
#                 else:
#                     test = test + plan[y]
#             # print(test)
#             if is_valid(test, keys):
#                 all.append(test)
#                 # print("VALID")
#                 first = test[0]
#                 last = test[len(test)-1]
#                 if first == '#' and last == '#':
#                     starth += 1
#                 elif first == '#' and last == '.':
#                     startd += 1
#                 elif first == '.' and last == '#':
#                     endinh += 1
#                 else:
#                     endind += 1
#                 result += 1
#                 ths+=1
#
#         # print(result)
#         r.append(ths)
#         poss = ['#', '.']
#
#
#
#
#     return all
#     #return starth, startd, endinh, endind
#
# def solution(lines):
#     patternss = ['hh', 'h.', '.h', '..']
#     length = 5
#     #patterns = generate_permutations_with_repetition(patternss, length)
#     #print(result)
#
#     sol = {
#         'hh': 0,
#         'h.': 1,
#         '.h': 2,
#         '..': 3
#     }
#
#     r=0
#
#     for x in range(len(lines)):
#         print("Line " + str(x))
#         nl = []
#         new_lines = []
#         new_lines2 = []
#         line = lines[x].strip()
#         values = line.split()
#         plan = values[0].strip()
#         key = values[1].strip()
#         keys = key.split(',')
#
#         nl.append((plan, key))
#
#         new_lines.append(('?' + plan, key))
#
#         new_lines2.append((plan + '?', key))
#
#         first = helper(nl, 1)
#         second = helper(new_lines, 1)
#         third = helper(new_lines2, 1)
#
#         options = []
#         options_s = []
#         for val in first:
#             options.append((val, 1, True, 1))
#             options_s.append((val, 1, True, 1))
#         for val in third:
#             options.append((val, 3, False, 1))
#             options_s.append((val, 1, True, 1))
#
#
#         memo = {}
#
#         while (len(options_s)) > 0:
#             option = options_s.pop()
#
#             if option
#
#             if option[1] == 1 or option[1] == 2:
#                 for next in second:
#                     if prune(option, next, keys, opt_set, h):
#                         new_options.append((option[0] + next, 2, option[2]))
#
#             if option[1] == 3:
#                 if h < 3:
#                     for val in third:
#                         if prune(option, val, keys, opt_set, h):
#                             new_options.append((option[0] + val, 3, option[2]))
#
#                     if not option[2]:
#                         for val in first:
#                             if prune(option, val, keys, opt_set, h):
#                                 new_options.append((option[0] + val, 1, True))
#                 else:
#                     if not option[2]:
#                         for val in first:
#                             if prune(option, val, keys, opt_set, h):
#                                 new_options.append((option[0] + val, 1, True))
#
#
#
#         # for h in range(4):
#         #     new_options = []
#         #     opt_set = set()
#         #     for option in options:
#         #         if option[1] == 1 or option[1] == 2:
#         #             for next in second:
#         #                 if prune(option, next, keys, opt_set, h):
#         #                     new_options.append((option[0] + next, 2, option[2]))
#         #
#         #         if option[1] == 3:
#         #             if h < 3:
#         #                 for val in third:
#         #                     if prune(option, val, keys, opt_set, h):
#         #                         new_options.append((option[0] + val, 3, option[2]))
#         #
#         #                 if not option[2]:
#         #                     for val in first:
#         #                         if prune(option, val, keys, opt_set, h):
#         #                             new_options.append((option[0] + val, 1, True))
#         #             else:
#         #                 if not option[2]:
#         #                     for val in first:
#         #                         if prune(option, val, keys, opt_set, h):
#         #                             new_options.append((option[0] + val, 1, True))
#         #     options = new_options
#         #
#         # r += len(options)
#     return r

def generate_permutations_of_hashes_and_dots(length):
    symbols = ['#', '.']
    permutations_list = list(product(symbols, repeat=length))
    return permutations_list

memo = {}

def count_possible(input, keys, times):
    
    if (input, times) in memo:
        return memo[(input, times)]
    
    plan = list(input)

    hc = 0
    q = []
    for y in range(len(plan)):
        if plan[y] == '?':
            q.append(y)
        elif plan[y] == '#':
            hc += 1

    t = 0
    for a in keys:
        t += int(a)
    
    if times == 1:
        possible_orders = generate_permutations_with_zeros_ones(t - hc, len(q) - (t - hc))
        
        result = []
        for order in possible_orders:
            for x in range(len(order)):
                plan[q[x]] = order[x]
                
            output = ""
            for x in plan:
                if x == 0:
                    output += '#'
                elif x == 1:
                    output += '.'
                else:
                    output += x
                
            if is_valid(output, keys):
                result.append(output)
        memo[(input, times)] = result
        return result
    
    if times > 1:
        combined = []
        combineds = set()
        
        
        for z in range(times - 1):
            result1 = count_possible(input + '?', keys, z + 1)    
            result2 = count_possible(input, keys, times - z - 1)
            
            result = []
            for a in range(len(result1)):
                for b in range(len(result2)):
                    if is_valid(result1[a] + result2[b], keys * times):
                        result.append(result1[a] + result2[b])
            
            for r in result:
                if r not in combineds:
                    combined.append(r)
                combineds.add(r)

            result1 = count_possible(input, keys, z + 1)
            result2 = count_possible('?' + input, keys, times - z - 1)

            result = []
            for a in range(len(result1)):
                for b in range(len(result2)):
                    temp = result1[a] + result2[b]
                    if temp not in combineds and is_valid(temp, keys * times):
                        combined.append(temp)
                        combineds.add(temp)

        memo[(input, times)] = combined
        return combined

if __name__ == '__main__':
    # if sys.argv[1] == 't':
    #     input = open("test.txt", "r")
    # else:
    #     input = open("input.txt", "r")
    # print(solution(input, 1))

    file = open("input.txt", "r")
    lines = file.readlines()

    total = 0
    for x in range(len(lines)):
        print("Line " + str(x))
        memo = {}
        line = lines[x].strip()
        values = line.split()
        plan = values[0].strip()
        key = values[1].strip()
        keys = key.split(',')
        total += len(count_possible(plan, keys, 5))
    print(total)

    # if sys.argv[1] == 't':
    #     input
    # else:
    #     input = open("input.txt", "r")
    # print(solution(input, 2))
    #
    # if sys.argv[1] == 't':
    #     input = open("test.txt", "r")
    # else:
    #     input = open("input.txt", "r")
    # print(solution(input, 3))