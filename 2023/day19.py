import time
import functools, itertools, collections, re
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd
from itertools import *
from pprint import pprint
from math import prod
import sys
sys.path.append("..")
from aocl import *
day = 19
puzzle = Puzzle(year=2023, day=day)
inp = """
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
""".strip()
inp = puzzle.input_data
res = 0

rules_, parts_ = inp.split("\n\n")
rules_,parts_ = rules_.split(), parts_.split()
parts = []
for p in parts_:
    p = p.strip("{}")
    parts.append(dict((m.split("=")[0], int(m.split("=")[1])) for m in p.split(",")))
workflows = dd(list)
d = {'x': 1679, 'm': 44, 'a': 3000, 's': 496}

for r in rules_:
    name, rr = r.split("{")
    rr = rr.strip("}").split(",")
    for rule in rr:
        if ":" in rule:
            cond_, dest = rule.split(":")
            cond = (cond_[0], cond_[1:])
            workflows[name].append([cond, dest])
        else:
            cond = None
            dest = rule
            workflows[name].append([cond, dest])
for item in parts:
    wf = "in"
    while wf not in ("A", "R"):
        print(item, wf)
        for cond, dest in workflows[wf]:
            y = cond is None or (eval(f"{item[cond[0]]}{cond[1]}"))
            if y:
                wf = dest
                break
        else: assert False
    if wf == "A":
        res += sum(item.values())

print(f"Solution: {res}\n")
# submit(res)

# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")