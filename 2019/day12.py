from collections import defaultdict
import math, itertools

def solve():
    pos = [[-1, 7, 3], [12, 2, -13], [14, 18, -8], [17, 4, -4]]
    # pos = [[-1, 0, 2], [2,-10, -7], [4, -8, 8], [3, 5, -1]]
    velocity = [[0,0,0], [0,0,0], [0,0,0], [0,0,0]]
    for i in range(1000):
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

            velocity[c[0]] = v1
            velocity[c[1]] = v2
        for k in range(4):
            pos[k] = [j + velocity[k][l] for l,j in enumerate(pos[k])]

    energy = 0
    for i in range(4):
        pot = sum(abs(x) for x in pos[i])
        kin = sum(abs(x) for x in velocity[i])
        energy += pot * kin

    return energy, None

a, b = solve()
print(f"Part 1: {a}") 
print(f"Part 2: {b}") 