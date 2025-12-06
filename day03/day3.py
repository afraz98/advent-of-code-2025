import timeit

def parse_input(filename):
    return [line.strip('\n') for line in open(filename, 'r')]

def solve_part_one():
    total = 0
    for line in parse_input("day3_test.txt"):
        for i in reversed(range(0, 10)):
            if line.count(str(i)) > 0:
                first_digit = i
                first_index = line.index(str(first_digit))
                break

        for j in reversed(range(0, first_digit)):
            if line.count(str(j)) > 0:
                second_digit = j
                second_index = line.index(str(second_digit))
                break

        if first_index > second_index:
            joltage = (10 * second_digit) + first_digit
        else:
            joltage = (10 * first_digit) + second_digit
        
        print(joltage)
        total += joltage
    print(total)
    pass

def solve_part_two():
    pass

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))

result = timeit.timeit('solve_part_two()', setup='from __main__ import solve_part_two', number=1)
print("Part II ran in %s seconds" % str(result))
