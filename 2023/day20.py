import time
import functools, itertools, collections, re
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd
from itertools import *
from pprint import pprint
from math import prod
from copy import deepcopy
import sys
sys.path.append("..")
from aocl import *
day = 20
puzzle = Puzzle(year=2023, day=day)
inp = """
%cd -> jx, gh
%bk -> jp, cn
%px -> xc, hg
%tv -> gh, xl
&xc -> bm, zq, jf, hg, bd, hn
%bd -> px
&bh -> mf
%dx -> cn, rb
%vv -> pp, gh
broadcaster -> cx, zq, tv, rh
%rb -> cn, qr
&jf -> mf
%jd -> mm
%cx -> xd, cn
%zs -> cz
%hn -> bm
%xr -> bd, xc
&mf -> rx
%zq -> kg, xc
&cn -> sh, jd, cx, tc, xd
%cs -> xj
%fb -> tc, cn
%mm -> cn, bk
%sq -> th, hz
%sz -> vx
%xl -> gh, sz
%vm -> gh, vv
%jp -> cn
%qr -> cn, jd
%bq -> xc, zv
&sh -> mf
%gz -> gs, hz
%qc -> qg, xc
%hg -> bq
%dt -> sq, hz
%xj -> fz
%qs -> gh
%fz -> hz, zs
%qg -> xc
%pp -> qs, gh
%zv -> xc, qc
%rh -> hz, mr
&gh -> tv, lk, sz, bh, vx
%th -> hz
&mz -> mf
%bm -> xr
%lk -> pg
%jx -> lk, gh
&hz -> xj, cs, zs, rh, mz
%tc -> dx
%mr -> hz, gz
%xd -> jk
%pg -> vm, gh
%kg -> hn, xc
%gs -> cs, hz
%vx -> cd
%cz -> hz, dt
%jk -> cn, fb
""".strip() # 896998430
# inp = """
# broadcaster -> a
# %a -> inv, con
# &inv -> b
# %b -> con
# &con -> output
# """.strip()
inp = puzzle.input_data

inp = lines(inp)
res = 0
graph = dd(list)
ffs, conjs = set(), set()
pred = None
for line in inp:
    module, dests = line.split(" -> ")
    t = module[0]
    module = module[1:] if module != "broadcaster" else module
    if t == "%": ffs.add(module)
    elif t == "&": conjs.add(module)
    dests = dests.split(", ")
    if dests == ["rx"]:
        assert pred is None and t == "&"
        pred = module
    graph[module].extend(dests)
print(graph)

stateff, statec = {}, {}
for node in conjs:
    statec[node] = dict((n, 0) for n, d in graph.items() if node in d)
for node in ffs:
    stateff[node] = False

low, high = 0, 0
last = dd(list)
cycles = {}
for i in range(1, 10000000):
    pulses_in = [("broadcaster", "button", 0)]
    low += 1
    while pulses_in:
        node, sender, pulse = pulses_in.pop(0)
        if node == pred and pulse == 1:
            last[sender].append(i)
            if len(last[sender]) > 1:
                cycles[sender] = last[sender][1] - last[sender][0]

        if len(cycles) == 4:
            print(prod(cycles.values()))
            exit()

        if node == "broadcaster":
            p = pulse
        elif node in ffs:
            if pulse == 1:
                continue
            stateff[node] = not stateff[node]
            p = int(stateff[node])
        elif node in conjs:
            statec[node][sender] = pulse
            p = int(any(p == 0 for origin, p in statec[node].items()))
        else:
            continue

        for c in graph[node]:
            pulses_in.append((c, node, p))
            low += p == 0
            high += p == 1

print(high, low)
print(f"Solution: {high*low}\n")
# submit(res)

# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")