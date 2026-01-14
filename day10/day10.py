import itertools
import timeit

def parse_input(filename : str) -> list[str]:
    return [line.strip('\n') for line in open(filename, 'r')]

def test_button_presses(buttons, number_lights) -> str:
    sequence = ["." for x in range(number_lights)]
    for button in buttons:
        for digit in button.split(","):
            sequence[int(digit)] = "#" if sequence[int(digit)] == "." else "."
    return ''.join(sequence)

def solve_part_one():
    """
    Find the fewest possible button presses required to properly configure
    each machine.

    Indicator light diagrams are bracketed, e.g. [.##.]
    Button wiring diagrams are within parenthesis, e.g. (3) (1,3) (2) (2,3)
    Joltage ratings are within braces, e.g. {3,5,4,7}
    """
    total_button_presses = 0
    machines = parse_input("day10.txt")

    for machine in machines:
        parts = machine.split(" ")
        lights = parts[0].strip("[]")
        buttons = [x.strip("()") for x in parts[1:-1]]
        joltages = [int(x) for x in parts[-1].strip("{}").split(",")]

        # Generate all possible combinations of buttons
        all_combinations = []
        for i in range(1, len(buttons) + 1):
            all_combinations.extend(itertools.combinations(buttons, i))

        # Sort by length (ascending)
        all_combinations.sort(key=lambda x : len(x))
        
        # If final pattern matches lights, return number of button presses
        for combination in all_combinations:
            if(test_button_presses(combination, len(lights)) == lights):
                print("Minimum presses was %d" % len(combination))
                total_button_presses += len(combination)
                break
    print(total_button_presses)
    pass

def solve_part_two():
    pass

result = timeit.timeit('solve_part_one()', setup='from __main__ import solve_part_one', number=1)
print("Part I ran in %s seconds" % str(result))

result = timeit.timeit('solve_part_two()', setup='from __main__ import solve_part_two', number=1)
print("Part II ran in %s seconds" % str(result))
