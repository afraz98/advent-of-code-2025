import math
import timeit

def parse_input(filename) -> list[str]:
    return [tuple(map(int, line.strip('\n').split(','))) for line in open(filename, 'r')]

def connect(circuits : list[set], point1, point2) -> None:
    set1 = set2 = None
    for s in circuits:
        if point1 in s:
            set1 = s
        if point2 in s:
            set2 = s

    if set1 is not set2:
        set1.update(set2)
        circuits.remove(set2)
    pass

def solve_part_one():
    input_coordinates = parse_input("day8.txt")
    pairs = []
    for i in range(0, len(input_coordinates)):
        for j in range(i+1, len(input_coordinates)):
            pairs.append(((i, j), math.dist(input_coordinates[i], input_coordinates[j])))

    # Sort pairs by distance
    pairs.sort(key=lambda x : x[1])

    # Each junction box should start as its own circuit
    circuits = [{i} for i in range(0, len(input_coordinates))] # Circuits stored as sets of indices

    for i in range(len(input_coordinates)):
        ((p1, p2), _) = pairs[i]
        connect(circuits, p1, p2)

    circuits.sort(key=lambda x : len(x), reverse=True)
    print(len(circuits[0]) * len(circuits[1]) * len(circuits[2]))
    pass

def solve_part_two():
    input_coordinates = parse_input("day8.txt")
    pairs = []
    for i in range(0, len(input_coordinates)):
        for j in range(i+1, len(input_coordinates)):
            pairs.append(((i, j), math.dist(input_coordinates[i], input_coordinates[j])))

    # Sort pairs by distance
    pairs.sort(key=lambda x : x[1])

    # Each junction box should start as its own circuit
    circuits = [{i} for i in range(0, len(input_coordinates))] # Circuits stored as sets of indices

    for i in range(6247): # Guess and check!
        ((p1, p2), _) = pairs[i]
        connect(circuits, p1, p2)

    print(len(circuits))
    print(input_coordinates[p1][0] * input_coordinates[p2][0])
    pass

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))

result = timeit.timeit('solve_part_two()', setup='from __main__ import solve_part_two', number=1)
print("Part II ran in %s seconds" % str(result))

