import timeit

def parse_input(filename):
    return [line.strip('\n') for line in open(filename, 'r')]

def solve_part_one():
    current_position = 50
    count = 0
    instructions = parse_input("day1.txt")
    for instruction in instructions:
        direction, movement = instruction[0], int(instruction[1:])
        current_position = (current_position + movement) % 100 if direction == 'R' else (current_position - movement) % 100
        if(current_position == 0):
            count += 1
    print(count)
    pass

def solve_part_two():
    current_position = 50
    count = 0
    instructions = parse_input("day1.txt")
    for instruction in instructions:
        direction, movement = instruction[0], int(instruction[1:])
        for i in range(0, movement):
            current_position = (current_position + 1) % 100 if direction == 'R' else (current_position - 1) % 100
            if(current_position == 0):
                count += 1
    print(count)
    pass

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))

result = timeit.timeit('solve_part_two()', setup='from __main__ import solve_part_two', number=1)
print("Part II ran in %s seconds" % str(result))