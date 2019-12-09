from datetime import datetime
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict

day = datetime.today().day
puzzle = Puzzle(year=2019, day=day)
input_data = puzzle.input_data

def intcode(data=input_data, prog_in=[1]):
    inp = defaultdict(int)
    inp.update({i: v for i,v in enumerate([int(i) for i in data.split(",")])})
    pointer = 0
    rel_base = 0
    op = str(inp[pointer]).zfill(5)
    opcode = int(op[-2:])
    modes = [int(x) for x in op[:3]]
    
    def args(num, pos = False):
        if modes[3-num] == 0:
            return inp[inp[pointer+num]] if not pos else inp[pointer+num]
        elif modes[3-num] == 2:
            return inp[rel_base + inp[pointer+num]] if not pos else rel_base + inp[pointer+num]
        else:
            return inp[pointer+num]

    while opcode != 99:
        if opcode == 1:
            inp[args(3, True)] = args(1) + args(2)
            pointer += 4
        elif opcode == 2:
            inp[args(3, True)] = args(1) * args(2)
            pointer += 4
        elif opcode == 3:
            inp[args(3, True)] = prog_in.pop()
            pointer += 2
        elif opcode == 4:
            yield args(1)
            pointer += 2
        elif opcode == 5:
            pointer = pointer + 3 if args(1) == 0 else args(2)
        elif opcode == 6:
            pointer = pointer + 3 if args(1) != 0 else args(2)
        elif opcode == 7:
            inp[args(3, True)] = 1 if args(1) < args(2) else 0
            pointer += 4
        elif opcode == 8:
            inp[args(3, True)] = 1 if args(1) == args(2) else 0
            pointer += 4
        elif opcode == 9:
            rel_base += args(1)
            pointer += 2

        op = str(inp[pointer]).zfill(5)
        opcode = int(op[-2:])
        modes = [int(x) for x in op[:3]]

    yield "END"

def solve(inp=input_data):
    return list(intcode(inp, [1]))[:-1], list(intcode(inp, [2]))[:-1]

test1 = "104,1125899906842624,99"
test2 = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
test3 = "1102,34915192,34915192,7,4,7,99,0"

a, b = solve()
print(f"Part 1: {a}")
if b: print(f"Part 2: {b}")