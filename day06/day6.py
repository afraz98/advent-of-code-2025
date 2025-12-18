import timeit

def parse_input(filename):
    return [line.strip('\n') for line in open(filename, 'r')]

def solve_part_one():
    total = 0

    x = [int(x) for x in parse_input("day6.txt")[0].split(" ") if x != '']
    y = [int(y) for y in parse_input("day6.txt")[1].split(" ") if y != '']
    z = [int(z) for z in parse_input("day6.txt")[2].split(" ") if z != '']
    w = [int(w) for w in parse_input("day6.txt")[3].split(" ") if w != '']
    operators = [o for o in parse_input("day6.txt")[4].split(" ") if o != '']

    for i in range(len(x)):
        res = 0
        if operators[i] == "*":
            res = x[i] * y[i] * z[i] * w[i]
        if operators[i] == "+":
            res = x[i] + y[i] + z[i] + w[i]
        total += res

    print(total)
    pass


def parse_input_part_two(filename):
    rows = [line.strip('\n') for line in open(filename, 'r')]
    cols = zip(*rows)
    problems = [''.join(x) for x in list(cols)]
    return split_list(problems, " "*5)

def split_list(lst : list, separator: str):
    split_lst = []
    sub_list = []
    for i in range(0, len(lst)):
        if(lst[i] == separator):
            split_lst.append(sub_list)
            sub_list = []
        else:
            sub_list.append(lst[i])
    split_lst.append(sub_list)
    return split_lst

def solve_part_two():
    problems = parse_input_part_two("day6.txt")
    operator = ""
    total = 0

    print(problems)
    for problem in problems:
        print(problem)
        res = 0
        # Look for operator
        for i in range(0, len(problem)):
            if "*" in problem[i]: # Multiplication
                problem[i] = problem[i].replace("*", "")
                operator = "*"
                break
            elif "+" in problem[i]: # Addition
                problem[i] = problem[i].replace("+", "")
                print(problem[i])
                operator = "+"
                break
        if operator == "+":
            for i in range(0, len(problem)):
                res += int(problem[i])
        elif operator == "*":
            res = 1
            for i in range(0, len(problem)):
                res *= int(problem[i])
        total += res

    print(total)
    pass

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))

result = timeit.timeit('solve_part_two()', setup='from __main__ import solve_part_two', number=1)
print("Part II ran in %s seconds" % str(result))

