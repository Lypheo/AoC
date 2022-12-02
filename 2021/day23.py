import time
import functools, itertools, collections, re
import numpy as np
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd
from itertools import *
from pprint import pprint
import sys
sys.setrecursionlimit(10000)

day = 23
puzzle = Puzzle(year=2021, day=day)
input_data = puzzle.input_data

def test(tests, solution, part):
    c = 1
    for i,o in tests.items():
        if o[part] and (ao := solution(i)) != o[part]:
            print(f"Testcase {c} failed:\n    Expected output: {o}\n    Actual output: {ao}\n")
            return False
        c += 1
    print(f"Tests successful!")
    return True

cm = 999999999999999999999
def solve_a(inp=input_data):
    inp = inp.splitlines()[2:4]
    amphis = []
    for k in range(3, 10, 2):
        for i in range(2):
            amphis.append([inp[i][k], k, i+1])
    costs = dict(A = 1, B = 10, C = 100, D = 1000)
    rooms = dict(A = 3, B = 5, C = 7, D = 9)

    def dist(v1, v2):
        return sum(abs(v1[i] - v2[i]) for i in range(len(v1)))

    complete = lambda amph: all(x == rooms[a] and y > 0 for a,x,y in amph)

    from functools import cache
    tupify = lambda l: tuple(tuple(x) for x in l)
    @cache
    def change(amphin, costin):
        global cm
        # print(depth)
        amphin = list(list(x) for x in amphin)
        if costin > cm:
            return 99999999999
        if complete(amphin):
            if costin < cm:
                print(costin)
            cm = min(cm, costin)
            return costin
        nxt = []
        hallway = [True] + [any(x == xx and yy == 0 for _,xx,yy in amphin) for x in range(1,12)] + [True]
        for a, x, y in amphin:
            amph = amphin.copy()
            amph.remove([a,x,y])
            if x == rooms[a] and (y == 2 or (y == 1 and [a, x, 2] in amph)):
                continue
            if y == 0:
                occupied = [aa for aa, xx, __ in amph if x == rooms[a]]
                if len(occupied) < 2 and all(aa == a for aa in occupied):
                    cost = dist([rooms[a],2-len(occupied)], [x,y]) * costs[a]
                    newamph = amph.copy()
                    newamph.append([a,rooms[a],2-len(occupied)])
                    return change(tupify(newamph), costin+cost)
                    # nxt.append([newamph, cost+costin])
            elif not any(x == xx and yy == y-1 for _,xx, yy in amph):#
                possible = set()
                xx = x
                while not hallway[xx]:
                    possible.add(xx)
                    xx += 1
                xx = x
                while not hallway[xx]:
                    possible.add(xx)
                    xx -= 1
                possible -= set(px for px in possible if px in rooms.values())
                for px in possible:
                    newamph = amph.copy()
                    newamph.append([a,px,0])
                    cost = dist([px, 0], [x, y]) * costs[a]
                    nxt.append([newamph, cost+costin])

        # pprint(nxt)
        # exit()
        return min(change(tupify(nx), nc) for nx, nc in nxt) if nxt else 999999999999
    # print(amphis)
    # return change(* [[['B', 3, 1],
    #                   ['A', 3, 2],
    #                   ['C', 5, 1],
    #                   ['D', 5, 2],
    #                   ['C', 7, 2],
    #                   ['D', 9, 1],
    #                   ['A', 9, 2],
    #                   ['B', 4, 0]],
    #                  40])
    return change(tupify(amphis), 0)

def solve_b(inp=input_data):
    return False

tests = {
    """#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########""" : [12521, None]
}

# test(tests, solve_a, 0)
a = solve_a()
print(f"Part 1: {a}\n")
# submit(int(a) if isinstance(a, float) else a, part="a", day=day, year=2021)

# test(tests, solve_b, 1)
# b = solve_b()
# print(f"Part 2: {b}")
# submit(int(b) if isinstance(b, float) else b, part="b", day=day, year=2021)
#
#
# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")