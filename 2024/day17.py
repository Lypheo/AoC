import time
import functools, itertools, collections, re
from aocd.models import Puzzle
import sys
sys.path.append("..")
from aocl import *

st=time.time()

puzzle = Puzzle(year=2024, day=17)
inp = puzzle.input_data

res = 0
Regs, Prog = blocks(inp)
Regs = [ints(line)[0] for line in lines(Regs)]
Prog = ints(Prog)

def ex(regs, prog):
    regs, prog = regs.copy(), prog.copy()
    def combo(op):
        return op if  op <= 3 else regs[op - 4]

    ip = 0
    out = []
    while ip < len(prog)-1:
        inst, op = prog[ip:ip+2]
        ip += 2
        match inst:
            case 0:
                regs[0] = int(regs[0] / (2**combo(op)))
            case 1:
                regs[1] = regs[1] ^ op
            case 2:
                regs[1] = combo(op) % 8
            case 3:
                if regs[0] != 0:
                    ip = op
            case 4:
                regs[1] = regs[1] ^ regs[2]
            case 5:
                out.append(combo(op) % 8)
            case 6:
                regs[1] = int(regs[0] / (2**combo(op)))
            case 7:
                regs[2] = int(regs[0] / (2**combo(op)))
    return out

"""
2,4,1,2,7,5,0,3,4,7,1,7,5,5,3,0
B <- A % 8
B <- B xor 010
C <- int(A / 2^B)
B <- B xor C
B <- B xor 111
print(B % 8)
A <- int(A / 8)
if A != 0:
    jmp 0
"""

res = 0
for x in Prog[::-1]:
    res *= 8
    while ex([res, 0,0], Prog)[0] != x:
        res += 1

print(f"Solution: {res}\n")
print(f"----{(time.time()-st):.3f} s----")

