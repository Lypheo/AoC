import functools
import re
from itertools import product
from numbers import Number
from functional import seq

def test(tests, solution, part):
    if len(tests) == 1 and not next(tests.keys()):
        return True
    c = 1
    for i,o in tests.items():
        if o[part] and (ao := solution(i)) != o[part]:
            print(f"Testcase {c} failed:\n    Expected output: {o[part]}\n    Actual output: {ao}\n")
            return False
        c += 1
    print(f"Tests successful!")
    return True

def mh_dist(a, b):
    if isinstance(a, tuple):
        return sum(abs(a[i] - b[i]) for i in range(len(a)))
    else:
        return int(abs(a.real - b.real) + abs(a.imag - b.imag))

def sr(a, b=None, step=1, inc=False): # signed range (because range() doesn’t handle start > end)
    if b is None:
        start, end = 0, a
    else:
        start, end = a, b
    if inc:
        end += 1 if end >= start else -1
    start, end = int(start), int(end)
    return range(start, end, step if end >= start else -step)

sri = lambda *args: sr(*args, inc=True) # signed range inclusive
srl = lambda *args: list(sr(*args)) # signed range list
sril = lambda *args: list(sri(*args)) # signed range inclusive list

def ip(st, e): # interpolate complex numbers, inclusive
    diff = e - st
    if diff.real == 0:
        for y in sri(int(diff.imag)):
            yield complex(st.real, st.imag + y)
    elif diff.imag == 0:
        for x in sri(int(diff.real)):
            yield complex(st.real + x, st.imag)
    elif abs(diff.imag) > abs(diff.real):
        for x in sri(int(diff.real)):
            yield complex(st.real + x, st.imag + x * diff.imag / diff.real)
    else:
        for y in sri(int(diff.imag)):
            yield complex(st.real + y * diff.real / diff.imag, st.imag + y)

ipl = lambda *args: list(ip(*args))

def tup_s(tp1, tp2):
    return tuple(a - b for a,b in zip(tp1, tp2))

def tup_a(tp1, tp2):
    return tuple(a + b for a,b in zip(tp1, tp2))

def pgrid(grid, empty = ".", zero = "top"): # print 2d grids indexed by complex numbers
    if isinstance(grid, dict):
        x1, x2 = min([p.real for p in grid.keys()]), max([p.real for p in grid.keys()])
        y1, y2 = min([p.imag for p in grid.keys()]), max([p.imag for p in grid.keys()])
        x1, x2, y1, y2 = map(int, [x1, x2, y1, y2])
        if zero != "top":
            y1, y2 = y2, y1
        for y in sri(y1, y2):
            for x in sri(x1, x2):
                print(grid.get(complex(x, y), empty), end="")
            print("")
        print("\n")
    else:
        x1, x2 = min([p.real for p in grid]), max([p.real for p in grid])
        y1, y2 = min([p.imag for p in grid]), max([p.imag for p in grid])
        x1, x2, y1, y2 = map(int, [x1, x2, y1, y2])
        if zero != "top":
            y1, y2 = y2, y1
        for y in sri(y1, y2):
            for x in sri(x1, x2):
                print("#" if complex(x,y) in grid else empty, end="")
            print("")
        print("\n")

diag_offsets = {}
for d in [2,3]:
    res = list(product(sri(-1, 1), repeat=d))
    res.remove(tuple(0 for _ in range(d)))
    diag_offsets[d] = res

straight_offsets = {}
for d in [2,3]:
    res = list(tuple(off if i == dim else 0 for i in range(d))
               for off, dim in product((-1, 1), range(d)))
    straight_offsets[d] = res
del res

straight_offsets_j = [complex(*off) for off in straight_offsets[2]]
diag_offsets_j = [complex(*off) for off in diag_offsets[2]]
def nb(p, diag=False): # neighbours
    assert isinstance(p, Number) or isinstance(p, tuple)
    if isinstance(p, Number):
        offs = diag_offsets_j if diag else straight_offsets_j
        return (p + off for off in offs)
    else:
        d = len(p)
        offs = diag_offsets[d] if diag else straight_offsets[d]
        return (tup_a(p, off) for off in offs)

nbd = lambda *args: nb(*args, diag=True) # neighbours diagonal
nbl = lambda *args: list(nb(*args)) # neighbours list
nbdl = lambda *args: list(nbd(*args)) # neighbours diagonal list
nbc, nbdc = functools.cache(nbl), functools.cache(nbdl)

def parse_grid(inp, to_int=False, to_set=False):
    inp = lines(inp) if isinstance(inp, str) else inp
    grid = dict()
    for y, line in enumerate(inp):
        for x, c in enumerate(line):
            grid[complex(x, y)] = c if not to_int else int(c)
    return grid if not to_set else {x for x in grid if grid[x] != "."}

def blocks(inp):
    return inp.split("\n\n")

def lines(inp):
    return inp.splitlines()

def ints(line):
    return [int(x) for x in re.findall(r"(-?\d+)", line)]

from functional.pipeline import extend

@extend()
def sfilter(it, f):
    return seq(it).filter(lambda t: f(*t))

@extend()
def sreduce(it, f):
    return seq(it).reduce(lambda t: f(*t))

from forbiddenfruit import curse
curse(object, "seq", lambda self: seq(self))