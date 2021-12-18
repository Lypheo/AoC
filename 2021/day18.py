import time
import functools, itertools, collections, re
import numpy as np
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd

day = 18
puzzle = Puzzle(year=2021, day=day)
input_data = puzzle.input_data

def test(tests, solution, part):
    c = 1
    for i,o in tests.items():
        if o[part] and (ao := solution(i)) != o[part]:
            print(f"Testcase {c} failed:\n    Expected output: {o}\n    Actual output: {ao}\n")
            return False
        c += 1
    print(f"Tests successful!")
    return True

def explode(num, depth):
    global add, n
    if isinstance(num, int):
        n += 1
        return num

    if depth >= 4 and not add:
        add.update([(n, num[0]), (n+2, num[1])])
        return 0

    return [explode(num[0], depth+1), explode(num[1], depth+1)]

def inc(num):
    global add, m
    if isinstance(num, int):
        m += 1
        if m in add:
            return num + add[m]
        return num
    return [inc(num[0]), inc(num[1])]

def split(num):
    global splat
    if isinstance(num, int):
        if num >= 10 and not splat:
            splat = True
            return [num//2, num//2 + (num % 2)]
        return num
    return [split(num[0]), split(num[1])]

def reduce(a,b):
    global n, m, add, splat
    pair = [a,b]
    actions = [lambda num: inc(explode(num, 0)), split]
    while True:
        for a in actions:
            add, n, m, splat = {}, -1, -1, False
            newp = a(pair)
            if pair != (pair := newp):
                break
        else:
            break
    return pair

def mag(num):
    if isinstance(num, int):
        return num
    return 3 * mag(num[0]) + 2* mag(num[1])

def solve_a(inp=input_data):
    numbers = [eval(x) for x in inp.splitlines()]
    from functools import reduce as red
    return mag(red(reduce, numbers))

def solve_b(inp=input_data):
    numbers = [eval(x) for x in inp.splitlines()]
    return max(mag(reduce(a, b)) for a,b in itertools.permutations(numbers, 2))

tests = {

    """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]""" : [4140, 3993]
}

test(tests, solve_a, 0)
# a = solve_a()
# print(f"Part 1: {a}\n")
# submit(int(a) if isinstance(a, float) else a, part="a", day=day, year=2021)

test(tests, solve_b, 1)
# b = solve_b()
# if b:
#     print(f"Part 2: {b}")
#     submit(int(b) if isinstance(b, float) else b, part="b", day=day, year=2021)
#
#
# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")