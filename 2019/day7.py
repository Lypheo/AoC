from datetime import datetime
from aocd.models import Puzzle
from aocd import submit
import itertools

day = datetime.today().day
puzzle = Puzzle(year=2019, day=day)
input_data = puzzle.input_data

def intcode(inp=input_data, prog_in=[1]):
    inp = [int(i) for i in inp.split(",")]
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
            inp[inp[pointer+1]] = prog_in.pop()
            pointer += 2
        elif opcode == 4:
            yield args(1)
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

    yield "END"

def solve(inp=input_data):
    p1 = lambda num, phase: intcode(inp, [p1(num-1, phase) if num != 0 else 0, phase[num]]).__next__()
    p1_max = max(p1(4, i) for i in itertools.permutations([0,1,2,3,4]))

    signals = []
    for i in  itertools.permutations([5, 6, 7, 8, 9]):
        proginp = [[i[j]] if j != 0 else [0, i[j]] for j in range(5)]
        progs = [intcode(inp, proginp[i]) for i in range(5)]
        while proginp[0][0] != "END":
            signal = proginp[0][0]
            for k in range(5):
                proginp[k+1 if k != 4 else 0].insert(0, next(progs[k]))
        signals.append(signal)
    return p1_max, max(signals)

test = "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"
a, b = solve()
print(f"Part 1: {a}")
print(f"Part 2: {b}")
