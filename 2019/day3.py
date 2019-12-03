from datetime import datetime
from aocd.models import Puzzle
from aocd import submit

day = datetime.today().day
puzzle = Puzzle(year=2019, day=day)
input_data = puzzle.input_data

def solve(inp=input_data):
    paths = [i.split(",") for i in inp.split("\n")]
    def walk(pos, move, used, steps):
        current_steps = steps[pos]
        count = int(move[1:])
        for _ in range(count):
            if move[0] == "U":
                pos = (pos[0], 1 + pos[1])
            elif move[0] == "R":
                    pos = (pos[0] + 1, pos[1])
            elif move[0] == "L":
                    pos = (pos[0] - 1, pos[1])
            elif move[0] == "D":
                    pos = (pos[0], pos[1] - 1)
            
            current_steps += 1
            used.add(pos)
            steps[pos] = current_steps
        return pos

    pos = [(0,0), (0,0)]
    stepsa, stepsb = {(0,0): 0}, {(0,0): 0}
    used_a = set()
    used_b = set()
    for moves in zip(*paths):
        pos[0] = walk(pos[0], moves[0], used_a, stepsa) 
        pos[1] = walk(pos[1], moves[1], used_b, stepsb)
    cross = list(used_a.intersection(used_b))
    return min([abs(x[0]) + abs(x[1]) for x in cross]), min([stepsa[i] + stepsb[i] for i in cross])

a, b = solve()
print(f"Part 1: {a}")
if b: print(f"Part 2: {b}")
# submit(a, part="a", day=day, year=2019)
# submit(b, part="b", day=day, year=2019)
