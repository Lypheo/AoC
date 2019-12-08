from datetime import datetime
from aocd.models import Puzzle
from aocd import submit
import timeit, time

day = datetime.today().day
puzzle = Puzzle(year=2019, day=day)
input_data = puzzle.input_data

def solve(inp=input_data):
    data = inp.splitlines()
    parents = {}
    for i in data:
        center, orbiter = i.split(")")
        parents[orbiter] = center

    def count_depth(center, depth):
        if center not in parents.keys():
            return depth
        else:
            print(center, depth)
            return count_depth(parents[center], depth + 1)

    print(count_depth(parents["L"], 1))
    orbits = sum(count_depth(parents[i], 1) for i in parents.keys())

    def search(current, last, transfers):
        if current not in parents.values():
            return 0
        elif current == parents["SAN"]:
            return transfers
        else:
            children = [k for k,v in parents.items() if (v == current and k != last)]
            downward = sum(search(i, "NONE", transfers+1) for i in children) 
            upward = search(parents[current], current, transfers+1) if (current != "COM" and last != "NONE") else 0
            return upward + downward

    distance = None#search(parents["YOU"], "YOU", 0)
    return orbits, distance

test = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""
solve(test)