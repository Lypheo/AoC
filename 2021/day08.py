import time
import functools, itertools, collections, re
import numpy as np
from aocd.models import Puzzle
from aocd import submit

day = 8
puzzle = Puzzle(year=2021, day=day)
input_data = puzzle.input_data

def test(tests, solution, part):
    for i,o in tests.items():
        if o[part] and (ao := solution(i)) != o[part]:
            print(f"Testcase failed:\n    Expected output: {o}\n    Actual output: {ao}\n")
            return False
    print(f"Tests successful!")
    return True

def solve_a(inp=input_data):
    inp = inp.splitlines()
    s = 0
    for l in inp:
        d, o = l.split(" | ")
        d = d.split()
        n = [7, 4, 2, 3]
        s += sum(len(k) in n for k in o.split())
    return s

def solve_b(inp=input_data):
    s = 0
    ug = [set(x) for x in ["abcefg","cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abdcfg"]]
    for l in inp.splitlines():
        w = re.findall(r"\w+", l)
        from itertools import permutations
        letters = "abcdefg"
        for p in permutations(range(7)):
            cm = {c: letters[mc] for c, mc in zip(letters, p)}
            if all(set(cm[c] for c in v) in ug for v in w):
                break

        od = [ug.index(set(cm[c] for c in v)) for v in w[-4:]]
        s += int("".join(map(str, od)))

    return s

tests = {
    """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce""" : [375, 61229],
    # """acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf""" : [1,5353]
}

# test(tests, solve_a, 0)
# a = solve_a()
# print(f"Part 1: {a}\n")
# submit(int(a) if isinstance(a, float) else a, part="a", day=day, year=2021)

test(tests, solve_b, 1)
# b = solve_b()
# if b:
#     print(f"Part 2: {b}")
    # submit(int(b) if isinstance(b, float) else b, part="b", day=day, year=2021)
#
#
# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")