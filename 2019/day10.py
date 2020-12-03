from datetime import datetime
from aocd.models import Puzzle
from aocd import submit
from timeit import timeit
import math

day = datetime.today().day
puzzle = Puzzle(year=2019, day=day)
input_data = puzzle.input_data

def solve(inp=input_data):
    grid = [list(row) for row in inp.splitlines()]

    def los(a, b, x, y):
        difx, dify = x-a, y-b
        gcd = math.gcd(difx, dify)
        dx, dy = difx//gcd, dify//gcd

        return any(grid[i*dy + b][i*dx + a] == "#" for i in range(1, gcd))

    def detect(a, b):
        return [(x,y) for y,row in enumerate(grid) for x, ast in enumerate(row) \
                        if ast != "." and (y != b or x != a) and los(a, b, x, y)]

    def angle(p, base):
        x, y = p[0] - base[0], base[1] - p[1]
        a = math.atan2(x, y)
        return 2*math.pi + a if a < 0 else a

    counts = [(x,y,len(detect(x, y))) for y,row in enumerate(grid) for x, ast in enumerate(row) if ast == "#"]
    best = max(counts, key=lambda x: x[2])
    station = best[:2]
    destroyed = []
    visible = detect(*station)
    while len(visible) != 0:
        destroy = sorted(visible, key=lambda p: angle(p, station))
        for x,y in destroy:
            grid[y][x] = "."
        destroyed.extend(destroy)
        visible = detect(*station)

    return best[2], destroyed[199]

a, b = solve()
print(f"Part 1: {a}") #314
print(f"Part 2: {b}") # 15, 13