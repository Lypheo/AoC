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
day = 15
puzzle = Puzzle(year=2023, day=day)
inp = """
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
""".strip()
inp = puzzle.input_data
#

# inp = lines(inp)
res = 0
def h(x):
    v = 0
    for c in x:
        v += ord(c)
        v *= 17
        v = v % 256
    return v
boxes = [[] for _ in range(256)]
for x in inp.split(","):
    label, num = re.split(r"[=-]", x)
    # print(label, num)
    boxid = h(label)
    box = boxes[boxid]
    if num:
        for ind, (l, fl) in enumerate(box):
            if l == label:
                box[ind][1] = num
                break
        else:
            box.append([label, num])
    else:
        box = [y for y in box if y[0] != label]
    boxes[boxid] = box

for i, box in enumerate(boxes, 1):
    print(box)
    res += sum(i * j * int(lens[1]) for j, lens in enumerate(box, 1))
print(f"Solution: {res}\n")
# submit(res)
#
# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")