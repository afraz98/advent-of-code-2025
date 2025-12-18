import timeit

def parse_input(filename):
    return [line.strip('\n') for line in open(filename, 'r')]

def solve_part_one():
    fresh = 0
    data = parse_input("day5.txt")
    ranges = data[:data.index("")]
    ids = data[data.index("")+1:]

    for id in ids:
        for rang in ranges:
            rmin, rmax = rang.split("-")[0], rang.split("-")[1]
            if int(id) >= int(rmin) and int(id) <= int(rmax):
                fresh += 1
                break
    print(fresh)
    pass

def solve_part_two():
    """
    Find total number of fresh ingredients across all ranges. 

    NOTE: Ranges may contain one another, so need to check if ranges are contained within each other
    """
    total = 0
    merged_ids = []
    data = parse_input("day5.txt")
    data = data[:data.index("")]
    ranges = sorted([(int(x.split("-")[0]), int(x.split("-")[1])) for x in data])

    merged_ids = [ranges[0]]
    for start, end in ranges[1:]:
        prev_start, prev_end = merged_ids[-1]
        if start <= prev_end:   # Ranges overlap
            merged_ids[-1] = (prev_start, max(prev_end, end))
        else:                   # Ranges do not overlap
            merged_ids.append((start, end))

    for r in merged_ids:
        total += r[1] - r[0] + 1
    print(total)
    pass

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))

result = timeit.timeit('solve_part_two()', setup='from __main__ import solve_part_two', number=1)
print("Part II ran in %s seconds" % str(result))

