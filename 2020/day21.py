import math
import time
from datetime import datetime
import time
import functools, itertools, collections, re
from math import ceil, prod, gcd
from collections import defaultdict
cprod = itertools.product

from aocd.models import Puzzle
from aocd import submit
from pprint import pprint

day = 21
puzzle = Puzzle(year=2020, day=day)
input_data = puzzle.input_data

def test(tests, solution):
    for i,o in tests.items():
        if (ao := solution(i)) not in o:
            print(f"Testcase failed:\nInput:\n{i}\nExpected output:\n    {o}\nActual output:\n    ", end="")
            pprint(ao)
            return False
    print(f"Tests successful!")
    return True

def solve_a(inp=input_data):
    l = []
    ingredients = defaultdict(int)
    for food in inp.split("\n"):
        ings, allergens = food.strip(")").split(" (contains ")
        ings, allergens = ings.split(" "), allergens.split(", ")
        l.append([ings, {a: set(ings) for a in allergens}])
        for i in ings:
            ingredients[i] += 1

    d = defaultdict(list)
    for e in l:
        allergens = e[1]
        for a,ings in allergens.items():
            d[a].append(ings)

    d = {k: set.intersection(*v) for k,v in d.items()}
    print(d)

    mappings = {k:v.pop() for k,v in d.items() if len(v) == 1}
    d = {k:v for k,v in d.items() if k not in mappings}

    while d:
        for mk, mv in mappings.items():
            for dk, dv in d.items():
                if mv in dv:
                    dv.remove(mv)
        mappings.update({k:v.pop() for k,v in d.items() if len(v) == 1})
        d = {k:v for k,v in d.items() if k not in mappings}

    safe = [ing for ing in ingredients.keys() if ing not in mappings.values()]
    return sum(v for k,v in ingredients.items() if k in safe)

def solve_b(inp=input_data):
    l = []
    ingredients = defaultdict(int)
    for food in inp.split("\n"):
        ings, allergens = food.strip(")").split(" (contains ")
        ings, allergens = ings.split(" "), allergens.split(", ")
        l.append([ings, {a: set(ings) for a in allergens}])
        for i in ings:
            ingredients[i] += 1

    d = defaultdict(list)
    for e in l:
        allergens = e[1]
        for a,ings in allergens.items():
            d[a].append(ings)

    d = {k: set.intersection(*v) for k,v in d.items()}
    "".strip()
    mappings = {k:v.pop() for k,v in d.items() if len(v) == 1}
    d = {k:v for k,v in d.items() if k not in mappings}
    while d:
        for mk, mv in mappings.items():
            for dk, dv in d.items():
                if mv in dv:
                    dv.remove(mv)
        mappings.update({k:v.pop() for k,v in d.items() if len(v) == 1})
        d = {k:v for k,v in d.items() if k not in mappings}

    return ",".join(mappings[k] for k in sorted(mappings.keys()))

tests = {
    """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)""": (5, "mxmxvkd,sqjhc,fvjkl")
}


# a = solve_a()
# print(f"Part 1: {a}\n")
test(tests, solve_a)
# submit(a, part="a", day=day, year=2020)

# b = solve_b()
# print(f"Part 2: {b}")
# test(tests, solve_b)
# submit(b, part="b", day=day, year=2020)

# t1 = time.time_ns()
# for i in range(times := 100):
#     solve_a()
# t2 = time.time_ns()
# print(f"Part 1: {(t2-t1)/(1000000*times)} ms")
#
# t1 = time.time_ns()
# for i in range(times := 100):
#     solve_b()
# t2 = time.time_ns()
# print(f"Part 2: {(t2-t1)/(1000000*times)} ms")