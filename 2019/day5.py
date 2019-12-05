from datetime import datetime
from aocd.models import Puzzle
from aocd import submit

day = datetime.today().day
puzzle = Puzzle(year=2019, day=day)
input_data = puzzle.input_data

def solve(inp=input_data, prog_in=1):
    inp = [int(i) for i in inp.split(",")]
    io = [prog_in]
    pointer = 0
    op = str(inp[pointer]).zfill(5)
    opcode = int(op[-2:])
    modes = [int(x) for x in op[:3]]
    args = lambda num: inp[pointer+num] if modes[3-num] else inp[inp[pointer+num]]
    while opcode != 99:
        if opcode == 1:
            inp[inp[pointer+3]] = args(1) + args(2)
            pointer += 4
        elif opcode == 2:
            inp[inp[pointer+3]] = args(1) * args(2)
            pointer += 4
        elif opcode == 3:
            inp[inp[pointer+1]] = io.pop()
            pointer += 2
        elif opcode == 4:
            print("Output: ", args(1))
            pointer += 2
        elif opcode == 5:
            pointer = pointer + 3 if args(1) == 0 else args(2)
        elif opcode == 6:
            pointer = pointer + 3 if args(1) != 0 else args(2)
        elif opcode == 7:
            inp[inp[pointer+3]] = 1 if args(1) < args(2) else 0
            pointer += 4
        elif opcode == 8:
            inp[inp[pointer+3]] = 1 if args(1) == args(2) else 0
            pointer += 4

        op = str(inp[pointer]).zfill(5)
        opcode = int(op[-2:])
        modes = [int(x) for x in op[:3]]

print("Part 1: ", solve(prog_in=1))
print("Part 2: ", solve(prog_in=5))

