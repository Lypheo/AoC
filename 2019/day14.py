from datetime import datetime
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict, Counter
import re, math

day = datetime.today().day
puzzle = Puzzle(year=2019, day=day)
input_data = puzzle.input_data

def solve(inp=input_data):
    reactions = defaultdict(int)
    for reaction in inp.splitlines():
        inputs, output = reaction.split("=>")
        inputs = tuple([tuple([int(ing.strip().split(" ")[0]), ing.strip().split(" ")[1]])  for ing in inputs.split(",")])
        output = [int(output.strip().split(" ")[0]), output.strip().split(" ")[1]]
        reactions[output[1]] = (output[0], inputs)

    direct = [i for i,v in reactions.items() if v[1][0][1] == "ORE"]

    def get_ore(count):
        c = Counter()
        excess = Counter()
        def count_ore(chemical, count):
            need = reactions[chemical][1]
            exc = (count % reactions[chemical][0])
            if excess[chemical] >= exc:
                count = math.floor(count / reactions[chemical][0])
                excess[chemical] -= exc
            else:
                count = math.ceil(count / reactions[chemical][0])
                excess[chemical] += reactions[chemical][0] - exc

            for i in need:
                if i[1] in direct:
                    c[i[1]] += (i[0] * count)
                else:
                    count_ore(i[1], i[0] * count)
        count_ore("FUEL", count)
        return sum(math.ceil(v / reactions[i][0]) * reactions[i][1][0][0] for i,v in c.items())

    def bisect(k=0, power = 9):
        ore = 0
        while ore < 1000000000000:
            k += 10 ** power
            ore = get_ore(k)
        if power == 0:
            return k-1
        else:
            return bisect(k- 10**power, power-1)

    return get_ore(1), bisect()

a, b = solve()
print(f"Part 1: {a}") 
print(f"Part 2: {b}") 