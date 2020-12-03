from datetime import datetime
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict
import itertools

day = datetime.today().day
puzzle = Puzzle(year=2019, day=day)
input_data = puzzle.input_data

def solve(inp=input_data):
    shuffle_instrctions = [("".join(i.split(" ")[:-1]), i.split(" ")[-1]) if i.split(" ")[-1].strip("-").isdecimal() else tuple([i.replace(" ", "")]) for i in inp.splitlines()]
    deck = list(range(10007))

    for i in shuffle_instrctions:
        if i[0] == "dealintonewstack":
            deck = list(reversed(deck))
        elif i[0] == "cut":
            n = int(i[1])
            top, bottom = deck[:n], deck[n:]
            deck = bottom + top
        elif i[0] == "dealwithincrement":
            n = int(i[1])
            new_deck = [None]*10007
            for i in range(len(deck)):
                new_deck[(i*n) % len(deck)] = deck[i]
            deck = new_deck

    return deck.index(2019), shuffle_instrctions

test = """deal with increment 7
deal with increment 9
cut -2"""

a, b = solve()
print(f"Part 1: {a}") 
print(f"Part 2: {b}") 
