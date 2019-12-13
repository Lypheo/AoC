from datetime import datetime
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict
import math, re

day = datetime.today().day
puzzle = Puzzle(year=2019, day=day)
input_data = puzzle.input_data

def getints(string):
    return [int(x) for x in re.findall(r"[-\d.]+", string)]

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
            inp[args(1, True)] = prog_in.pop()
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

    while True:
        yield "END"

def solve(inp=input_data):
    inp = "2" + inp[1:]
    grid = defaultdict(int)
    prog_in = []
    game = intcode(inp, prog_in)
    ball, paddle, blocks = None, None, 0
    while True:
        x, y, tile = next(game), next(game), next(game)
        if x == "END":
            break

        if x == -1 and y == 0:
            score = tile
        else:
            grid[(x, y)] = tile
            if tile == 4:
                ball = x
            elif tile == 3:
                paddle = x

        if ball and paddle:
            prog_in.clear()
            prog_in.append(0 if paddle == ball else (ball - paddle) / abs(ball-paddle))
        else:
            blocks = list(grid.values()).count(2)

    return blocks, score

a, b = solve()
print(f"Part 1: {a}") 
print(f"Part 2: {b}") 