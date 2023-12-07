import time
import functools, itertools, collections, re
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd
from itertools import *
from pprint import pprint
from math import prod
import sys
sys.path.append("..")
from aocl import *
day = 7
puzzle = Puzzle(year=2023, day=day)
inp = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
""".strip()
inp = puzzle.input_data


inp = lines(inp)
res = 0
card_strength = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
lst = []

def get_type(hand):
    size = len(set(hand))
    count = max(hand.count(x) for x in set(hand))

    match (size, count):
        case 1,_:
            typ = 1
        case 2, 4:
            typ = 2
        case 2, 3:
            typ = 3
        case 3, 3:
            typ = 4
        case 3, 2:
            typ = 5
        case 4, 2:
            typ = 6
        case 5,_:
            typ = 7
    return typ

for l in inp:
    hand, bid = l.split(" ")
    bid = int(bid)
    orig = hand
    min_typ = get_type(hand)
    for comb in product(card_strength, repeat=hand.count("J")):
        hand = orig
        for c in comb:
            hand = hand.replace("J", c, 1)
            typ = get_type(hand)
            if typ < min_typ:
                min_typ = typ

    lst.append((orig, bid, min_typ))

from functools import cmp_to_key
def cmp1(hand1, hand2):
    if hand1[2] < hand2[2]:
        return -1
    elif hand1[2] > hand2[2]:
        return 1
    for c1, c2 in zip(hand1[0], hand2[0]):
        if card_strength.index(c1) < card_strength.index(c2):
            return -1
        elif card_strength.index(c1) > card_strength.index(c2):
            return 1
    return 0
lst = sorted(lst, key=cmp_to_key(cmp1), reverse=True)
res = sum([i*hand[1] for i,hand in enumerate(lst, 1)])
print(f"Solution: {res}\n")
# submit(res)

# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")