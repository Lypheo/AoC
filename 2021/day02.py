from aocd.models import Puzzle

day = 2
puzzle = Puzzle(year=2021, day=day)
input_data = puzzle.input_data

def solve_a(inp=input_data):
    inp = inp.splitlines()
    pos = 0j
    for l in inp:
        v = int(l.split()[1])
        if l.startswith("forward"):
            pos += v
        elif l.startswith("up"):
            pos += v*1j
        else:
            pos += v*-1j
    return int(pos.real) * -int(pos.imag)

def solve_b(inp=input_data):
    inp = inp.splitlines()
    pos = 0j
    aim = 0
    for l in inp:
        v = int(l.split()[1])
        if l.startswith("forward"):
            pos += v
            pos += aim*v*1j
        elif l.startswith("up"):
            aim -= v
        else:
            aim += v
    return int(pos.real) * int(pos.imag)

a = solve_a()
print(f"Part 1: {a}\n")

b = solve_b()
print(f"Part 2: {b}")
