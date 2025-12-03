import timeit

def parse_input(filename):
    return [line.strip('\n') for line in open(filename, 'r')]

def check_sequence(id_range):
    acc = 0
    low, high = int(id_range[0]), int(id_range[1])
    for i in range(low, high+1):
        for j in list(reversed(range(0, len(str(i))))):
            if str(i)[:j] == str(i)[j:]:
                acc += i
    return acc

"""
For a given range of numbers n-m, check for repeated sequences in numbers, e.g. 11, 1010, 10001000, etc.
The sequence 11-22 has two of these numbers (11 and 22)
"""
def solve_part_one():
    acc = 0
    id_ranges = [x.split("-") for x in parse_input("day2.txt")[0].split(",")]
    for r in id_ranges:
        acc += check_sequence(r)
    print(acc)
    pass

def solve_part_two():
    pass

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))

result = timeit.timeit('solve_part_two()', setup='from __main__ import solve_part_two', number=1)
print("Part II ran in %s seconds" % str(result))