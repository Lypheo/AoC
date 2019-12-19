from datetime import datetime
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict
import itertools
import numpy as np
# import networkx as nx
# import re, sys
# sys.setrecursionlimit(2000)

day = datetime.today().day
puzzle = Puzzle(year=2019, day=day)
input_data = puzzle.input_data

def getints(string):
    import re
    return [int(x) for x in re.findall(r"[-\d.]+", string)]

def intcode(data=input_data, prog_in=[1]):
    inp = defaultdict(int)
    inp.update({i: v for i,v in enumerate([int(i) for i in data. split(",")])})
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

    yield "END"

def draw(grid):
    minx = int(min(z.real for z in grid.keys()))
    maxx = int(max(z.real for z in grid.keys()))
    miny = int(min(z.imag for z in grid.keys()))
    maxy = int(max(z.imag for z in grid.keys()))
    for y in reversed(range(miny, maxy+1)):
        for x in range(minx, maxx+1):
            val = grid[complex(x, y)]
            print(val if val != 0 else " ", end="")
        print("\n", end="")
    print("\n\n", end="")

def solve(inp=input_data):
    prog_in = []
    robot = intcode(inp, prog_in)
    grid = defaultdict(int)
    pos = 0j
    while True:
        char = next(robot)
        if char == "END":
            break
        elif char == 10:
            pos = complex(0, pos.imag - 1)
            continue
        
        pos += 1
        grid[pos] = chr(char)

    draw(grid)
    intersections = 0
    for z in grid.copy().keys():
        if grid[z] != "#":
            continue
        inters = True
        for i in (z+1j**i for i in range(4)):
            if grid[i] != "#":
                inters = False
        if inters:
            intersections += (z.real-1) * abs(z.imag)

    movements = []
    dir_map = [1j, 1+0j, -1j, -1+0j]
    pos = [k for k,v in grid.items() if v == "^"][0]
    direction = 1j
    while True:
        if grid[pos + direction] != "#":
            for i in ("L", "R"):
                new_dir = dir_map[ (dir_map.index(direction) + (-1 if i == "L" else 1)) % 4]
                if grid[pos + new_dir] == "#":
                    movements.extend([i, 0])
                    direction = new_dir
                    break
            if grid[pos + direction] != "#": #no path either left or right -> terminate
                break

        while grid[pos + direction] == "#":
            pos += direction
            movements[-1] += 1

    movements = list(zip(movements[::2], movements[1::2]))
    print(movements)

    def rem_sublist(arr, subarr):
        delete = []
        subarr = tuple(subarr)
        for i in range(len(arr)-len(subarr)+1):
            if tuple(arr[i:i+len(subarr)]) == subarr:
                delete.append((i,i+len(subarr)))
                
        delete = sorted(delete, key=lambda x: x[0])
        out = arr.copy()
        offset = 0
        for i in delete:
            overlap = False
            for k in delete:
                if i[0] > k[0] and i[0] <= k[1]:
                    overlap = True
            if not overlap:
                del out[offset+i[0]:offset+i[1]]
                offset += i[0]-i[1]
        return out

    def sublists(lst):
        return [lst[k:k+i+1] for i in range(len(lst)) for k in range(len(lst)-i)]

    def find_funcs(movements):
        for l in range(1, 20):
            fun1 = movements[:l]
            mov1 = rem_sublist(movements, fun1)
            mem_used = (len(movements) - len(mov1))*2 + sum(4 if g[1] < 10 else 5 for g in fun1) - 1
            print(mem_used)
            for l2 in range(1, 21 - mem_used):
                fun2 = mov1[:l2]
                mov2 = rem_sublist(mov1, fun2)
                mem_used += (len(mov1) - len(mov2))*2 + sum(4 if g[1] < 10 else 5 for g in fun2) - 1
                for l3 in range(1, 21 - mem_used):
                    fun3 = mov2[:l3]
                    mov3 = rem_sublist(mov2, fun3)
                    mem_used += (len(mov2) - len(mov3))*2 + sum(4 if g[1] < 10 else 5 for g in fun3) - 2
                    if mem_used <= 20:
                        return [fun1, fun2, fun3]

    return intersections, find_funcs(movements)

a, b = solve()
print(f"Part 1: {a}") 
print(f"Part 2: {b}") # nowhere near functional lol
