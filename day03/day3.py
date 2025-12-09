import timeit

def parse_input(filename):
    return [line.strip('\n') for line in open(filename, 'r')]

def calculate_joltage_part_one(joltages : str):
    max_joltage = 0
    for i in range(0, len(joltages)):
        for j in range(i+1, len(joltages)):
            new_joltage = (10 * int(joltages[i])) + int(joltages[j])
            if  new_joltage > max_joltage:
                max_joltage = new_joltage 
    return max_joltage

def solve_part_one():
    """
    Determine the maximum joltage rating obtained by switching on two batteries. 
    NOTE: Batteries must be switched on in sequential order.

    Idea: Iterate to the right from each position, maintain "max" joltage rating that will 
        be added to the total after entire sequence traversed, e.g.

        987654321111111 98 -> 97 -> 96 ... 91 ...
                        87 -> 86 -> 85 ... 81 ... 11
    """
    print(sum([calculate_joltage_part_one(line) for line in parse_input("day3.txt")]))
    pass

def calculate_joltage_part_two(joltages : list, sequence_length : int):
    rating = 0
    for i in reversed(range(1, sequence_length)):
        local_max = max(joltages[:-i])
        rating += 10**i * local_max
        joltages = joltages[joltages.index(local_max)+1:]
    return rating

def solve_part_two():
    """
    Determine the maximum joltage rating obtained by switching on **twelve** batteries. 
    NOTE: Batteries must be switched on in sequential order.

    Inspired by this implementation: https://github.com/githuib/advent-of-code/blob/master/src/advent_of_code/year2025/day03.py
    """
    print(sum([calculate_joltage_part_two([int(x) for x in line], 12) for line in parse_input("day3.txt")]))
    pass

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))

result = timeit.timeit('solve_part_two()', setup='from __main__ import solve_part_two', number=1)
print("Part II ran in %s seconds" % str(result))

