import timeit

def parse_input(filename):
    return [line.strip('\n') for line in open(filename, 'r')]

def _check_repeated_sequence(id : int):
    for j in list(reversed(range(0, len(str(id))))):
        if str(id)[:j] == str(id)[j:]:
            return True
    return False

def check_repeated_sequence(id_range):
    """
    Check if a range of numbers contains any number that contains a repeated sequence of digits.
    """
    acc = 0
    low, high = int(id_range[0]), int(id_range[1])
    for i in range(low, high+1):
        if _check_repeated_sequence(i):
            acc += i
    return acc

def solve_part_one():
    """
    For a given range of numbers n-m, check for repeated sequences in numbers, e.g. 11, 1010, 10001000, etc.
    The sequence 11-22 has two of these numbers (11 and 22)
    """
    acc = 0
    id_ranges = [x.split("-") for x in parse_input("day2.txt")[0].split(",")]
    for r in id_ranges:
        acc += check_repeated_sequence(r)
    print(acc)
    pass

def chunk(string, length):
    return [string[i : (length+i)] for i in range(0, len(string), length)]

def check_non_repeating_sequence(id : int):
    for i in range(1, len(str(id))):
        chunks = chunk(str(id), i)
        if chunks.count(chunks[0]) == len(chunks):
            return True
    return False

def check_repeating_sequence(id_range):
    """
    Check if a range of numbers contains any number that is entirely composed of repeated sequenc(es) or digit(s.
    
    IDEA: Split string into N equal parts, make sure all parts are equal for some value of N
    
    Args:
        id_range (list(str)): IDs as list of strings, e.g. ["11", "22"]
    """
    acc = 0
    low, high = int(id_range[0]), int(id_range[1])
    for i in range(low, high+1):
        if check_non_repeating_sequence(i):
            acc += i
    return acc

def solve_part_two():
    """
    For a given range of numbers n-m, check for one of more digits repeated twice. 
    For example, the sequence 998-1012 contains two invalid IDs: 999 and 1010.

    NOTE: The number should ONLY be made of repeating sequences. This means numbers such as 
        2121212118 and 2121212124 are valid.
    """
    acc = 0
    id_ranges = [x.split("-") for x in parse_input("day2.txt")[0].split(",")]
    for r in id_ranges:
        acc += check_repeating_sequence(r)
    print(acc)
    pass

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))

result = timeit.timeit('solve_part_two()', setup='from __main__ import solve_part_two', number=1)
print("Part II ran in %s seconds" % str(result))
