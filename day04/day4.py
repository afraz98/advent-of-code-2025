import timeit

def parse_input(filename):
    return [line.strip('\n') for line in open(filename, 'r')]

def _check_access(row, col, grid):
    if row > len(grid)-1 or row < 0:
        return 0
    if col > len(grid[0])-1 or col < 0:
        return 0
    if grid[row][col] == ".":
        return 0
    return 1

def check_access(row, col, grid):
    if(grid[row][col] == "."):
        return 5
    return _check_access(row+1, col, grid) + _check_access(row-1, col, grid) + \
            _check_access(row, col+1, grid) + _check_access(row, col-1, grid) +  _check_access(row+1, col-1, grid) + \
            _check_access(row-1, col+1, grid) + _check_access(row+1, col+1, grid) + _check_access(row-1, col-1, grid)

def solve_part_one():
    total = 0
    grid = [list(x) for x in parse_input("day4.txt")]
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            total = (total + 1) if check_access(row, col, grid) < 4 else total
    print(total)
    pass

def solve_part_two():
    total_rolls_removed = 0
    grid = [list(x) for x in parse_input("day4.txt")]

    while True:
        rolls_removed = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if check_access(row, col, grid) < 4:
                    grid[row][col] = "."
                    rolls_removed += 1
        total_rolls_removed += rolls_removed
        if rolls_removed == 0:
            break
    print(total_rolls_removed)

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))

result = timeit.timeit('solve_part_two()', setup='from __main__ import solve_part_two', number=1)
print("Part II ran in %s seconds" % str(result))

