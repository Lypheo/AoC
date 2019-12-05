from datetime import datetime
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict

day = datetime.today().day
puzzle = Puzzle(year=2019, day=day)
input_data = puzzle.input_data

def solve(inp=input_data):
    inp = [int(i) for i in inp.split(",")]
    iobuffer = [5]
    pointer = 0
    op = str(inp[pointer]).zfill(5)
    opcode = int(op[-2:])
    modes = [int(x) for x in op[:3]]
    while opcode != 99:
        # print(opcode, pointer, modes)
        # print(inp)
        if opcode == 1:
            inp[inp[pointer+3]] = inp[inp[pointer+1] if not modes[2] else pointer+1] + inp[inp[pointer+2] if not modes[1] else pointer+2]
            pointer += 4
        elif opcode == 2:
            inp[inp[pointer+3]] = inp[inp[pointer+1] if not modes[2] else pointer+1] * inp[inp[pointer+2] if not modes[1] else pointer+2]
            pointer += 4
        elif opcode == 3:
            inp[inp[pointer+1]] = iobuffer.pop()
            pointer += 2
        elif opcode == 4:
            print("Output: ", inp[inp[pointer+1]] if not modes[2] else inp[pointer+1])
            pointer += 2
        elif opcode == 5:
            first = inp[pointer+1] if modes[2] else inp[inp[pointer+1]]
            second = inp[pointer+2] if modes[1] else inp[inp[pointer+2]]
            pointer = pointer + 3 if first == 0 else second
        elif opcode == 6:
            first = inp[pointer+1] if modes[2] else inp[inp[pointer+1]]
            second = inp[pointer+2] if modes[1] else inp[inp[pointer+2]]
            pointer = pointer + 3 if first != 0 else second
        elif opcode == 7:
            first = inp[pointer+1] if modes[2] else inp[inp[pointer+1]]
            second = inp[pointer+2] if modes[1] else inp[inp[pointer+2]]
            inp[inp[pointer+3]] = 1 if first < second else 0
            pointer += 4
        elif opcode == 8:
            first = inp[pointer+1] if modes[2] else inp[inp[pointer+1]]
            second = inp[pointer+2] if modes[1] else inp[inp[pointer+2]]
            inp[inp[pointer+3]] = 1 if first == second else 0
            pointer += 4

        op = str(inp[pointer]).zfill(5)
        opcode = int(op[-2:])
        modes = [int(x) for x in op[:3]]
    return None, None




a, b = solve()
print(f"Part 1: {a}")
print(f"Part 2: {b}")
# submit(a, part="a", day=day, year=2019)
# submit(b, part="b", day=day, year=2019)