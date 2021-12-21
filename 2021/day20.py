import time
import functools, itertools, collections, re
import numpy as np
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd
from itertools import *

day = 20
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

def solve_a(inp=input_data):
    algo, image = inp.split("\n\n")
    img = set()
    for y, row in enumerate(image.split("\n")):
        for x, pixel in enumerate(row):
            if pixel == "#":
                img.add((x,y))

    boundsx = [min(k[0] for k in img), max(k[0] for k in img)+1]
    boundsy = [min(k[1] for k in img), max(k[1] for k in img)+1]

    for i in range(2):
        boundsx = [boundsx[0]-1, boundsx[1]+1]
        boundsy = [boundsy[0]-1, boundsy[1]+1]

        newimg = set()
        for px in range(*boundsx):
            for py in range(*boundsy):
                p = (px, py)
                bstr = ""
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        newp = (p[0] + dx, p[1] + dy)
                        bstr += "1" if newp in img else "0"

                b = int(bstr, 2)
                if algo[b] == "#":
                    newimg.add(p)

        if algo[0] == "#":
            if i % 2 == 0:
                for px in range(boundsx[0]-2, boundsx[1]+2):
                    for py in range(boundsy[0]-2, boundsy[1]+2):
                        if not (px >= boundsx[0] and px <= boundsx[1]-1 and py >= boundsy[0] and py <= boundsy[1]-1):
                            newimg.add((px, py))
            else:
                for px, py in newimg.copy():
                    if not (px >= boundsx[0] and px <= boundsx[1]-1 and py >= boundsy[0] and py <= boundsy[1]-1):
                        newimg.remove((px, py))
        img = newimg
        # for py in range(min(k[1] for k in img)-1, max(k[1] for k in img)+2):
        #     for px in range(min(k[0] for k in img)-1, max(k[0] for k in img)+2):
        #         if (px, py) in img:
        #             print("#", end="")
        #         else:
        #             print(".", end="")
        #     print("")

    return len(img)

def solve_b(inp=input_data):
    algo, image = inp.split("\n\n")
    img = set()
    for y, row in enumerate(image.split("\n")):
        for x, pixel in enumerate(row):
            if pixel == "#":
                img.add((x,y))

    boundsx = [min(k[0] for k in img), max(k[0] for k in img)+1]
    boundsy = [min(k[1] for k in img), max(k[1] for k in img)+1]

    for i in range(50):
        boundsx = [boundsx[0]-1, boundsx[1]+1]
        boundsy = [boundsy[0]-1, boundsy[1]+1]

        newimg = set()
        for px in range(*boundsx):
            for py in range(*boundsy):
                p = (px, py)
                bstr = ""
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        newp = (p[0] + dx, p[1] + dy)
                        bstr += "1" if newp in img else "0"

                b = int(bstr, 2)
                if algo[b] == "#":
                    newimg.add(p)

        if algo[0] == "#":
            if i % 2 == 0:
                for px in range(boundsx[0]-2, boundsx[1]+2):
                    for py in range(boundsy[0]-2, boundsy[1]+2):
                        if not (px >= boundsx[0] and px <= boundsx[1]-1 and py >= boundsy[0] and py <= boundsy[1]-1):
                            newimg.add((px, py))
            else:
                for px, py in newimg.copy():
                    if not (px >= boundsx[0] and px <= boundsx[1]-1 and py >= boundsy[0] and py <= boundsy[1]-1):
                        newimg.remove((px, py))
        img = newimg
    return len(img)

tests = {
    """#.#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#...

#..#.
#....
##..#
..#..
..###""" : [35, 3351]
}

test(tests, solve_a, 0)
# a = solve_a()
# print(f"Part 1: {a}\n")
# submit(int(a) if isinstance(a, float) else a, part="a", day=day, year=2021)

test(tests, solve_b, 1)
# b = solve_b()
# print(f"Part 2: {b}")
# submit(int(b) if isinstance(b, float) else b, part="b", day=day, year=2021)
#

import time
t1 = time.time_ns()
for i in range(times := 1):
    solve_b()
t2 = time.time_ns()
print(f"Time: {(t2-t1)/(1000000*times)} ms")