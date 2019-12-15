from datetime import datetime
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict

day = datetime.today().day
puzzle = Puzzle(year=2019, day=11)
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

    yield "END"

def solve(inp=input_data):
    grid = defaultdict(int)
    prog_in = []
    robot = intcode(inp, prog_in)
    direction = 0
    pos = (0,0)
    grid[pos] = 1
    while True:
        prog_in.append(grid[pos])
        paint = next(robot)
        if paint == "END": break
        grid[pos] = paint
        turn = next(robot)

        direction = (direction + 90 if turn == 1 else direction - 90) % 360
        if direction == 0: pos = (pos[0], pos[1]+1)
        elif direction == 90: pos = (pos[0]+1, pos[1])
        elif direction == 180: pos = (pos[0], pos[1]-1)
        elif direction == 270: pos = (pos[0]-1, pos[1])

    panels = len(grid)
    minpanel = (min(grid.keys(), key=lambda x: x[0])[0], min(grid.keys(), key=lambda x: x[1])[1])
    maxpanel = (max(grid.keys(), key=lambda x: x[0])[0], max(grid.keys(), key=lambda x: x[1])[1])
    out = [["   "]* (maxpanel[0] - minpanel[0] +1) for i in range((maxpanel[1] - minpanel[1] +1))]
    print(minpanel, maxpanel)
    for k,v in grid.items():
        if v == 1:
            out[k[1]+5][k[0]] = "###"
    for i in reversed(out):
        for j in i:
            print(j, end="")
        print("\n")

    return panels, None

a, b = solve()
print(f"Part 1: {a}") 
print(f"Part 2: {b}")