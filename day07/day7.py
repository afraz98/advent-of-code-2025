import timeit

def parse_input(filename):
    return [line.strip('\n') for line in open(filename, 'r')]

grid = [list(line) for line in parse_input("day7.txt")]
visited = [[False for element in lst] for lst in grid]

def traverse_path(grid, row, col):
    if row >= len(grid):
        return 0
    if col >= len(grid[0]) or col < 0:
        return 0
    if visited[row][col]:
        return 0
    
    visited[row][col] = True

    if(grid[row][col] == '^'):
        grid[row][col] = "!"
        return 1 + traverse_path(grid, row, col+1) + traverse_path(grid, row, col-1)

    return traverse_path(grid, row+1, col)

def solve_part_one():
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "S":
                start_row, start_col = row, col
    print(traverse_path(grid, start_row, start_col))
    pass

def solve_part_two():
    pass

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))

result = timeit.timeit('solve_part_two()', setup='from __main__ import solve_part_two', number=1)
print("Part II ran in %s seconds" % str(result))

