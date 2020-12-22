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

day = 22
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
    deck1, deck2 = [[int(x) for x in deck.split("\n")[1:]] for deck in inp.split("\n\n")]
    while deck1 and deck2:
        played = [deck1.pop(0), deck2.pop(0)]
        if played[0] > played[1]:
            deck1 += sorted(played, reverse=True)
        else:
            deck2 += sorted(played, reverse=True)

    winner = deck1 if deck1 else deck2
    return sum(winner[i-1]*(len(winner)+1-i) for i in range(1, len(winner)+1))

def solve_b(inp=input_data):
    def score(deck):
        return sum(deck[i-1]*(len(deck)+1-i) for i in range(1, len(deck)+1))

    def game(deck1: list, deck2):
        states = set()
        while True:
            if deck1 == [] or deck2 == []:
                break

            if (state := (tuple(deck1), tuple(deck2))) in states:
                return 0, score(deck1)
            else:
                states.add(state)

            played = [deck1.pop(0), deck2.pop(0)]
            if played[0] <= len(deck1) and played[1] <= len(deck2):
                winner, _ = game(deck1[:played[0]].copy(), deck2[:played[1]].copy())
            else:
                winner = int(played[0] < played[1])

            if winner == 1:
                deck2 += [played.pop(winner), played[0]]
            else:
                deck1 += [played.pop(winner), played[0]]

        return winner, score(deck2 if winner else deck1)




    deck1, deck2 = [[int(x) for x in deck.split("\n")[1:]] for deck in inp.split("\n\n")]
    winner, score = game(deck1, deck2)
    return score

tests = {
    """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10""": (306, 291)
}


# a = solve_a()
# print(f"Part 1: {a}\n")
test(tests, solve_a)
# submit(a, part="a", day=day, year=2020)

# b = solve_b()
# print(f"Part 2: {b}")
test(tests, solve_b)
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