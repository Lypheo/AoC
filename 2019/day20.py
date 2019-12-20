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
    nodes = [Node(start, [start + 1j**i for i in range(4) if grid[start + 1j**i] in string.ascii_uppercase][0], 0)]
    counter = 0
    while True:
        old_nodes = nodes.copy()
        nodes.clear()
        print(counter)
        for n in old_nodes:
            if n.pos == end and n.level == 0:
                return shortest_path_length(G, start, end), counter
            if n.level > 25:
                continue
            adjacent = [n.pos + 1j**i for i in range(4)]
            adjacent.remove(n.last)
            for i in adjacent:
                if i in tiles:
                    nodes.append(Node(i, n.pos, n.level))
                elif i in portal_cs_outer and n.level != 0:
                    nodes.append(Node(portals_inner[portals[i]][1], portals_inner[portals[i]][0], n.level-1))
                elif i in portal_cs_inner:
                    nodes.append(Node(portals_outer[portals[i]][1], portals_outer[portals[i]][0], n.level+1))

        counter += 1

a, b = solve()
print(f"Part 1: {a}") 
print(f"Part 2: {b}") 
