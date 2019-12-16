from datetime import datetime
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict
import networkx as nx
import sys
sys.setrecursionlimit(2000)
from PIL import Image

day = datetime.today().day
puzzle = Puzzle(year=2019, day=day)
input_data = puzzle.input_data

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

mov_map = {1:1j, 2:-1j, 3:-1, 4:1}
rev_map = {1:2, 2:1, 3:4, 4:3}

def solve(inp=input_data):
    prog_in = []
    robot = intcode(inp, prog_in)
    grid = defaultdict(int)
    grid[0j] = "."

    oxygen = None
    def floodfill(pos):
        
        for i in [1,2,3,4]:
            pos += mov_map[i]
            if grid[pos] != 0:
                pos -= mov_map[i]
                continue
            prog_in.append(i)
            reply = next(robot)
            if reply == 0:
                grid[pos] = "#"
                pos -= mov_map[i]
                continue
            elif reply == 2:
                grid[pos] = "O"
                nonlocal oxygen
                oxygen = pos
            elif reply == 1:
                grid[pos] = "."

            floodfill(pos)
            prog_in.append(rev_map[i])
            next(robot)
            pos -= mov_map[i]

    floodfill(0j)
    # import solution:

    # G = nx.Graph()
    # G.add_nodes_from(k for k,v in grid.items() if v in ("O", "."))
    # for k,v in grid.items():
    #     if v in ("O", "."):
    #         adjacent = [k-1, k+1, k-1j, k+1j]
    #         adjacent_path = [i for i in adjacent if i in grid and grid[i] in (".", "O")]
    #         G.add_edges_from((k, i) for i in adjacent_path)

    # dkstra = nx.algorithms.shortest_paths.generic.shortest_path_length
    # paths = [dkstra(G, oxygen, g) for g in G.nodes]
    # return dkstra(G, 0j, oxygen), max(paths)

    # proper solution:

    def search(pos, depth, visited):
        if pos == oxygen:
            return True
        elif depth == 0:
            return False

        visited.add(pos)
        adjacent = [pos-1, pos+1, pos-1j, pos+1j]
        adjacent_walkable = [i for i in adjacent if grid[i] in (".", "O") and i not in visited]
        return any(search(k, depth-1, visited) for k in adjacent_walkable)

    depth = 1
    while not search(0j, depth, set()):
        depth += 1

    time = 0
    filled = set([oxygen])
    size = sum(v in ("O", ".") for v in grid.values())
    while len(filled) < size:
        adjacent = []
        for k in grid.keys():
            if k in filled:
                adjacent.extend(i for i in (k+1j**i for i in range(4)) if i in grid and grid[i] == ".")
        filled.update(adjacent)
        time += 1

    return depth, time

a, b = solve(input_data)
print(f"Part 1: {a}") 
print(f"Part 2: {b}") 
