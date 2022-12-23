import re


def test(tests, solution, part):
    c = 1
    for i,o in tests.items():
        if o[part] and (ao := solution(i)) != o[part]:
            print(f"Testcase {c} failed:\n    Expected output: {o[part]}\n    Actual output: {ao}\n")
            return False
        c += 1
    print(f"Tests successful!")
    return True

mh_dist = lambda a,b: int(abs(a.real - b.real) + abs(a.imag - b.imag))

def sr(a, b=None, step=1, inc=False): # signed range
    if b == None:
        start, end = 0, a
    else:
        start, end = a, b
    if inc:
        end += 1 if end >= start else -1
    return range(start, end, step if end >= start else -step)

def ip(st, e): # interpolate complex numbers
    diff = e - st
    rng = []
    if diff.real == 0:
        rng = [complex(st.real, st.imag + y) for y in sr(int(diff.imag), inc=True)]
    elif diff.imag == 0:
        rng = [complex(st.real + x, st.imag) for x in sr(int(diff.real), inc=True)]
    elif abs(diff.imag) > abs(diff.real):
        for x in sr(int(diff.real), inc=True):
            rng.append(complex(st.real + x, st.imag + x * diff.imag / diff.real))
    else:
        for y in sr(int(diff.imag), inc=True):
            rng.append(complex(st.real + y * diff.real / diff.imag, st.imag + y))
    return rng

def ints(line):
    return [int(x) for x in re.findall("(-?\d+)", line)]


def tup_s(tp1, tp2):
    return tuple(a - b for a,b in zip(tp1, tp2))

def tup_a(tp1, tp2):
    return tuple(a + b for a,b in zip(tp1, tp2))

def pgrid(grid, empty = ".", zero = "top", t = "grid"):
    if t == "grid":
        x1, x2 = min([p.real for p in grid.keys()]), max([p.real for p in grid.keys()])
        y1, y2 = min([p.imag for p in grid.keys()]), max([p.imag for p in grid.keys()])
        x1, x2, y1, y2 = map(int, [x1, x2, y1, y2])
        if zero != "top":
            y1, y2 = y2, y1
        for y in sr(y1, y2, inc=True):
            for x in sr(x1, x2, inc=True):
                print(grid.get(complex(x, y), empty), end="")
            print("")
        print("\n")
    else:
        x1, x2 = min([p.real for p in grid]), max([p.real for p in grid])
        y1, y2 = min([p.imag for p in grid]), max([p.imag for p in grid])
        x1, x2, y1, y2 = map(int, [x1, x2, y1, y2])
        if zero != "top":
            y1, y2 = y2, y1
        for y in sr(y1, y2, inc=True):
            for x in sr(x1, x2, inc=True):
                print("#" if complex(x,y) in grid else empty, end="")
            print("")
        print("\n")