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
    ranges = []
    data = parse_input("day5_test.txt")
    input_ranges = data[:data.index("")]
    parsed_ranges = []

    for r in input_ranges:
        parsed_ranges.append((int(r.split("-")[0]), int(r.split("-")[1])))

    parsed_ranges = sorted(parsed_ranges)
    print(parsed_ranges)
    modified = True
    for rang in parsed_ranges:
        rang_min, rang_max = rang[0], rang[1]
        for r in list(parsed_ranges):
            rmin, rmax = r[0], r[1]
            print("Testing <%d, %d> against <%d, %d>" % (rang[0], rang[1], rmin, rmax))

            if rang_min >= rmin:
                if rmax >= rang_max: # Entire range contained in other range, remove range from list
                    print("<%d, %d> contains entirety of <%d, %d>" % (rmin, rmax, rang_min, rang_max))
                    modified = True
                    ranges.remove((rang_min, rang_max))
                elif rmax < rang_max: # Range has a higher maximum, update max
                    print("Max should be updated")
                    modified = True
                    rmax = rang_max
            elif rang_max >= rmin and rang_max <= rmax: # Ranges overlap
                print("Ranges overlap, extend")
                modified = True
                rmin = rang_min
                ranges.remove((rang_min, rang_max))
        print(parsed_ranges)
    print(sum([m - n + 1 for (n,m) in ranges]))
    pass

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))

result = timeit.timeit('solve_part_two()', setup='from __main__ import solve_part_two', number=1)
print("Part II ran in %s seconds" % str(result))

