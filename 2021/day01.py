from aocd.models import Puzzle

day = 1
puzzle = Puzzle(year=2021, day=day)
input_data = puzzle.input_data

def solve_a(inp=input_data):
    inp = [int(n) for n in inp.splitlines()]
    c = 0
    for i in range(1, len(inp)):
        if inp[i] > inp[i-1]:
            c += 1
    return c

def solve_b(inp=input_data):
    inp = [int(n) for n in inp.splitlines()]
    windows = [inp[i:i+3] for i in range(len(inp)-2)]
    c = 0
    for i,_ in enumerate(windows[1:]):
        if sum(windows[i]) > sum(windows[i-1]):
            c += 1
    return c

a = solve_a()
print(f"Part 1: {a}\n")
b = solve_b()
print(f"Part 2: {b}")
