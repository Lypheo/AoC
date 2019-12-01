from datetime import datetime
from aocd.models import Puzzle
from aocd import submit

day = datetime.today().day
puzzle = Puzzle(year=2019, day=day)
input_data = puzzle.input_data

def solve_a(inp=input_data):
    return sum([int(i) // 3 - 2 for i in inp.split("\n")])

def solve_b(inp=input_data):
    def get_fuel(mass):
        fuel = mass // 3 - 2
        return 0 if fuel < 1 else fuel + get_fuel(fuel)

    masses = [int(i) // 3 - 2 for i in inp.split("\n")]
    return sum([get_fuel(mass) + mass for mass in masses])

a = solve_a()
print(f"Part 1: {a}")
# submit(a, part="a", day=day, year=2019)

b = solve_b()
if b: print(f"Part 2: {b}")
# submit(b, part="b", day=day, year=2019)
