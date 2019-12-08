from datetime import datetime
from aocd.models import Puzzle

day = datetime.today().day
puzzle = Puzzle(year=2019, day=day)
input_data = puzzle.input_data

def solve(inp=input_data):
    layers = []
    i = 0
    length = 25 * 6
    while inp != "":
        layers.append([int(x) for x in inp[:length]])
        inp = inp[length*(i+1):]

    fewest_zeros = min(layers, key= lambda x: x.count(0))
    print("Part 1: {}".format( fewest_zeros.count(1) * fewest_zeros.count(2) ))

    packed = [[l[i] for l in layers if l[i] != 2] for i in range(length)]
    out = [packed[i][0] for i in range(length)]

    for j in range(6):
        for i in range(25):
            print("|||" if out[j*25+i] else "   ", end="")
        print("")

solve()