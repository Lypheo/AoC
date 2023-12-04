import re
from itertools import product
from numbers import Number

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

def nb(p, diag=False): # neighbours
    if isinstance(p, Number):
        offsets = (complex(*off) for off in nb((0,0), diag))
        for off in offsets:
            yield p + off
    elif isinstance(p, tuple):
        d = len(p)
        if diag:
            for off in product(sri(-1, 1), repeat=d):
                if off != tuple(0 for _ in range(d)):
                    yield tup_a(p, off)
        else:
            for off, dim in product((-1, 1), range(d)):
                yield tup_a(p, tuple(off if i == dim else 0 for i in range(d)))
    else:
        raise Exception("wrong type bro")

nbd = lambda *args: nb(*args, diag=True) # neighbours diagonal
nbl = lambda *args: list(nbl(*args)) # neighbours list
nbdl = lambda *args: list(nbd(*args)) # neighbours diagonal list

def parse_grid(inp):
    grid = dict()
    for y, line in enumerate(inp):
        for x, c in enumerate(line):
            grid[complex(x, y)] = c
    return grid

def blocks(inp):
    return inp.split("\n\n")

def lines(inp):
    return inp.splitlines()

def ints(line):
    return [int(x) for x in re.findall(r"(-?\d+)", line)]