import timeit

def parse_input(filename : str) -> list[str]:
    return [line.strip('\n') for line in open(filename, 'r')]

def calculate_rectangle_area(x1 : int, x2 : int, y1 : int, y2 : int):
    return (abs(y2 - y1) + 1) * (abs(x2 - x1) + 1)

def solve_part_one():
    areas = []
    coordinates = parse_input("day9.txt")
    for i in range(0, len(coordinates)):
        for j in range(i+1, len(coordinates)):
            x1,y1 = [int(x) for x in coordinates[i].split(",")]
            x2,y2 = [int(y) for y in coordinates[j].split(",")]
            areas.append(calculate_rectangle_area(x1,x2,y1,y2))
    print(max(areas))

def point_in_polygon(polygon_vertices : list[int], x : int, y : int):
    # Ray-casting point-in-polygon algorithm
    # Implementation described here: https://www.eecs.umich.edu/courses/eecs380/HANDOUTS/PROJ2/InsidePoly.html
    for px, py in polygon_vertices:
        pass
    return False

def calculate_rectangle_area_part_two(x1 : int, x2 : int, y1 : int, y2 : int):
    # TODO: Check if both rectangle edges are enclosed within polygon edges
    #       Consider using point-in-polygon or polygon intersection algorithm?
    return -1

def solve_part_two():
    areas = []
    vertices = [[int(y) for y in x.split(",")] for x in parse_input("day9.txt")]
    print(vertices)
    pass

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))

result = timeit.timeit('solve_part_two()', setup='from __main__ import solve_part_two', number=1)
print("Part II ran in %s seconds" % str(result))

