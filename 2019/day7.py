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
    signals = []
    for i in  itertools.permutations([5, 6, 7, 8, 9]):
        proginp = [[i[j]] for j in range(5)]
        proginp[0].insert(0, 0)
        progs = [intcode(inp, proginp[i]) for i in range(5)]
        while True:
            for k in range(5):
                o = next(progs[k])
                print(k, o)
                proginp[k+1 if k != 4 else 0].insert(0, o)
            if proginp[0][0] == "END":
                break
            else:
                signal = proginp[0][0]

        signals.append(signal)
    return max(signals), None

test = "3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10"
a, b = solve()
print(f"Part 2: {a}")
