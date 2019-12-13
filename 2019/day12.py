from collections import defaultdict
import math, itertools, timeit

input_data = """<x=-1, y=7, z=3>
<x=12, y=2, z=-13>
<x=14, y=18, z=-8>
<x=17, y=4, z=-4>"""

def getints(string):
    import re
    return [int(x) for x in re.findall(r"[-\d.]+", string)]

def solve(inp):
    pos = [getints(i) for i in inp.splitlines()]
    # pos = [[-1, 0, 2], [2,-10, -7], [4, -8, 8], [3, 5, -1]] # test input
    velocity = [[0,0,0], [0,0,0], [0,0,0], [0,0,0]]
    hist = [set(), set(), set()]
    cycle = [None]*3

    def lcm(a, b):
        return a * b // math.gcd(a, b)

    for n in itertools.count(0):
        states = [( tuple(p[i] for p in pos), tuple(v[i] for v in velocity) ) if cycle[i] == None else None for i in range(3)]
        for i in range(3):
            if cycle[i] == None and states[i] in hist[i]:
                cycle[i] = n
            else:
                hist[i].add(states[i])

        if not None in cycle:
            break

        if n == 1000:
            energy = sum(sum(abs(x) for x in pos[i]) * sum(abs(x) for x in velocity[i]) for i in range(4))

        for c in itertools.combinations([0,1,2,3], 2):
            p1, p2 = pos[c[0]], pos[c[1]]
            v1, v2 = velocity[c[0]], velocity[c[1]]
            for axis in range(3):
                if p1[axis] > p2[axis]:
                    v1[axis] += -1
                    v2[axis] += 1
                elif p1[axis] < p2[axis]:
                    v1[axis] += 1
                    v2[axis] += -1

        for k in range(4):
            pos[k] = [ p+v for p,v in zip(pos[k],velocity[k])]

    return energy, lcm(lcm(*cycle[:2]), cycle[2])

a, b = solve(input_data)
print(f"Part 1: {a}") 
print(f"Part 2: {b}") 

# print(timeit.timeit(solve, number = 5)/5)
