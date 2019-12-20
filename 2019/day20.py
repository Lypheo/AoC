from datetime import datetime
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict, namedtuple
import itertools, string
import networkx as nx
from networkx.algorithms.shortest_paths.generic import shortest_path_length

day = datetime.today().day
puzzle = Puzzle(year=2019, day=day)
input_data = puzzle.input_data

test1 = """             Z L X W       C                 
             Z P Q B       K                 
  ###########.#.#.#.#######.###############  
  #...#.......#.#.......#.#.......#.#.#...#  
  ###.#.#.#.#.#.#.#.###.#.#.#######.#.#.###  
  #.#...#.#.#...#.#.#...#...#...#.#.......#  
  #.###.#######.###.###.#.###.###.#.#######  
  #...#.......#.#...#...#.............#...#  
  #.#########.#######.#.#######.#######.###  
  #...#.#    F       R I       Z    #.#.#.#  
  #.###.#    D       E C       H    #.#.#.#  
  #.#...#                           #...#.#  
  #.###.#                           #.###.#  
  #.#....OA                       WB..#.#..ZH
  #.###.#                           #.#.#.#  
CJ......#                           #.....#  
  #######                           #######  
  #.#....CK                         #......IC
  #.###.#                           #.###.#  
  #.....#                           #...#.#  
  ###.###                           #.#.#.#  
XF....#.#                         RF..#.#.#  
  #####.#                           #######  
  #......CJ                       NM..#...#  
  ###.#.#                           #.###.#  
RE....#.#                           #......RF
  ###.###        X   X       L      #.#.#.#  
  #.....#        F   Q       P      #.#.#.#  
  ###.###########.###.#######.#########.###  
  #.....#...#.....#.......#...#.....#.#...#  
  #####.#.###.#######.#######.###.###.#.#.#  
  #.......#.......#.#.#.#.#...#...#...#.#.#  
  #####.###.#####.#.#.#.#.###.###.#.###.###  
  #.......#.....#.#...#...............#...#  
  #############.#.#.###.###################  
               A O F   N                     
               A A D   M                    """

def intcode(data, prog_in):
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

    yield "END"

def draw(grid):
    minx = int(min(z.real for z in grid.keys()))
    maxx = int(max(z.real for z in grid.keys()))
    miny = int(min(z.imag for z in grid.keys()))
    maxy = int(max(z.imag for z in grid.keys()))
    for y in range(miny, maxy+1):
        for x in range(minx, maxx+1):
            val = grid[complex(x, y)]
            print(val if val != 0 else " ", end="")
        print("\n", end="")
    print("\n\n", end="")

def solve(inp=input_data):
    grid = defaultdict(int)
    grid.update({complex(x, y): v for y, row in enumerate(inp.splitlines()) for x,v in enumerate(row)})
    w,h = len(inp.splitlines()[0]), len(inp.splitlines())
    
    G = nx.Graph()
    G.add_nodes_from(k for k,v in grid.items() if v ==".")

    portals_outer = defaultdict(int)
    portals_inner = defaultdict(int)
    portals = defaultdict(int)
    for n,v in grid.items():
        if v != ".":
            continue
        for i in [n-1, n+1, n-1j, n+1j]:
            if i in grid:
                if grid[i] == ".":
                    G.add_edge(n, i)
                elif grid[i] in string.ascii_uppercase:
                    second = [k for k in [i-1, i+1, i-1j, i+1j] if k in grid and grid[k] in string.ascii_uppercase][0]
                    portal = tuple(sorted([grid[i], grid[second]]))
                    if portal == tuple(sorted("AA")):
                        start = n
                    elif portal == tuple(sorted("ZZ")):
                        end = n
                    else:
                        portals[i] = portal
                        if i.real < 2 or i.real > w - 3 or i.imag < 2 or i.imag > h -3:
                            portals_outer[portal] = (i,n)
                        else:
                            portals_inner[portal] = (i,n)

    G.add_edges_from((c[1], portals_outer[p][1]) for p,c in portals_inner.items())

    portal_cs_inner = list(zip(*portals_inner.values()))[0]
    portal_cs_outer = list(zip(*portals_outer.values()))[0]
    tiles = [k for k,i in grid.items() if i == "."]

    Node = namedtuple("Node", ["pos", "last", "level"])
    nodes = [Node(start, None, 0)]
    counter = 0
    visited = set()
    while True:
        old_nodes = nodes.copy()
        nodes.clear()
        print(len(visited))
        for n in old_nodes:
            visited.add(n.pos)
            if n.pos == end and n.level == 0:
                return shortest_path_length(G, start, end), counter
            adjacent = [n.pos + 1j**i for i in range(4)]
            for i in adjacent:
                if i in tiles and i != n.last:
                    nodes.append(Node(i, n.pos, n.level))
                elif i in portal_cs_outer and n.level != 0:
                    nodes.append(Node(portals_inner[portals[i]][1], portals_inner[portals[i]][0], n.level-1))
                elif i in portal_cs_inner:
                    nodes.append(Node(portals_outer[portals[i]][1], portals_inner[portals[i]][0], n.level+1))

        counter += 1

a, b = solve(test1)
print(f"Part 1: {a}") 
print(f"Part 2: {b}") 
