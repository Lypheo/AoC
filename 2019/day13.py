from collections import defaultdict
import math, re

input_data = open(r"C:\Users\saifu\.config\aocd\53616c7465645f5fcfda96a9db2c5883a9e05e2606d444ec87b50db4c32ba1aa72106960361cec7f70bb1febdffcd66a\2019_13_input.txt").read()[:-1]
# input_data = open(r"C:\Users\saifu\Downloads\input").read()[:-1])

def intcode(data=input_data, prog_in=[1]):
    inp = defaultdict(int)
    inp.update({i: v for i,v in enumerate([int(i) for i in data.split(",")])})
    pointer = 0
    rel_base = 0
    op = inp[pointer]
    opcode = op % 100
    modes = [(op % 10**(x+1))//(10**x) for x in reversed(range(2, 5))]
    
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

        op = inp[pointer]
        opcode = op % 100
        modes = [(op % 10**(x+1))//(10**x) for x in reversed(range(2, 5))]

    while True:
        yield "END"

tilemap = [" ", "||", "#", "_", "O"]

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
            continue

        grid[(x, y)] = tile
        if tile == 4:
            ball = x
        if tile == 3:
            paddle = x

        if ball and paddle:
            prog_in.clear()
            prog_in.append(0 if paddle == ball else (ball - paddle) / abs(ball-paddle))
        else:
            blocks = list(grid.values()).count(2)

        # max_x = max(x[0] for x in grid.keys())
        # max_y = max(x[1] for x in grid.keys())
        
        # if 4 in list(grid.values()) and 3 in list(grid.values()):
        #     out = ""
        #     for row in range(max_y+1):
        #         out += "".join( tilemap[grid[(i, row)]] for i in range(max_x+1) ) + "\n"
        #     print(out)
        #     print("\033c", end="")

    return blocks, score

a, b = solve()
print(f"Part 1: {a}") 
print(f"Part 2: {b}") 
from timeit import timeit
# print(timeit(solve, number = 1))