import time
import functools, itertools, collections, re
from aocd.models import Puzzle
from aocd import submit
from collections import defaultdict as dd
from itertools import *
from pprint import pprint
import sys
sys.path.append("..")
from aocl import *
day = 19
puzzle = Puzzle(year=2022, day=day)
input_data = puzzle.input_data

def rt(tp, n, r):
    return (*tp[:n], tp[n] + r, *tp[n+1:])


def solve_a(inp=input_data):
    inp = inp.splitlines()
    bps = {}
    for line in inp:
        id, ore, clay, obs1, obs2, geo1, geo2 = ints(line)
        bps[id] = (ore, clay, (obs1, obs2), (geo1, geo2))

    # # @functools.cache
    # def gen_builds(ore, clay, obs, geo, bp):
    #     args = []
    #     if ore >= bp[0]:
    #         args.append(((1, 0, 0, 0), ore - bp[0], clay, obs, geo))
    #     if ore >= bp[1]:
    #         args.append(((0, 1, 0, 0), ore - bp[1], clay, obs, geo))
    #     if ore >= bp[3][0] and obs >= bp[3][1]:
    #         return [((0, 0, 0, 1), ore - bp[3][0], clay, obs - bp[3][1], geo)]
    #     if ore >= bp[2][0] and clay >= bp[2][1]:
    #         return [((0, 0, 1, 0), ore - bp[2][0], clay - bp[2][1], obs, geo)]
    #     return args + [((0,0,0,0), ore, clay, obs, geo)]
    #
    # @functools.cache
    # def f(material, robots, t, bpid):
    #     if t == 0:
    #         return material[-1]
    #
    #     mined = [0,0,0,0]
    #     possible_builds = gen_builds(*material, bps[bpid])
    #     for i, rob in enumerate(robots):
    #         mined[i] += rob
    #     M = 0
    #     for builds, ore, clay, obs, geo in possible_builds:
    #         new_robs = tup_a(builds, robots)
    #         new_mat = tup_a(tuple(mined), (ore, clay, obs, geo))
    #         M = max(M, f(new_mat, new_robs, t - 1, bpid))
    #     return M

    ans = 0
    for id, bp in bps.items():
        robots = (1, 0, 0, 0)
        material = (0, 0, 0, 0)
        states = {(robots, material)}
        for t in range(1, 25):
            new_states = set()
            for robots, material in states:
                ore, clay, obs, geo = material
                if ore >= bp[3][0] and obs >= bp[3][1]:
                    newm = (ore - bp[3][0], clay, obs - bp[3][1], geo)
                    newm = tuple(m + rob for m, rob in zip(newm, robots))
                    newr = rt(robots, 3, 1)
                    new_states.add((newr, newm))
                else:
                    new_states.add((robots, tuple(m + rob for m, rob in zip(material, robots))))
                    if ore >= bp[2][0] and clay >= bp[2][1]:
                        newm = (ore - bp[2][0], clay - bp[2][1], obs, geo)
                        newm = tuple(m + rob for m, rob in zip(newm, robots))
                        newr = rt(robots, 2, 1)
                        new_states.add((newr, newm))
                    if ore >= bp[0]:
                        newm = (ore - bp[0], clay, obs, geo)
                        newm = tuple(m + rob for m, rob in zip(newm, robots))
                        newr = rt(robots, 0, 1)
                        new_states.add((newr, newm))
                    if ore >= bp[1]:
                        newm = (ore - bp[1], clay, obs, geo)
                        newm = tuple(m + rob for m, rob in zip(newm, robots))
                        newr = rt(robots, 1, 1)
                        new_states.add((newr, newm))


            states = new_states
            # I changed a lot around this part of the code as it was running and I dont know which version produced the correct answer, so this might be wrong
            Mg = max(s[1][-1] for s in states)
            if Mg:
                states = {s for s in states if s[1][-1] >= Mg}

            print(t, len(states))
        quality = max([material[-1] for r, material in states])
        print(quality)
        ans += id * quality

    return ans

def solve_b(inp=input_data):
    inp = inp.splitlines()
    bps = {}
    for line in inp[:3]:
        id, ore, clay, obs1, obs2, geo1, geo2 = ints(line)
        bps[id] = (ore, clay, (obs1, obs2), (geo1, geo2))

    ans = 1
    for id, bp in bps.items():
        robots = (1, 0, 0, 0)
        material = (0, 0, 0, 0)
        states = {(robots, material)}
        for t in range(1, 33):
            new_states = set()
            for robots, material in states:
                ore, clay, obs, geo = material
                if ore >= bp[3][0] and obs >= bp[3][1]:
                    newm = (ore - bp[3][0], clay, obs - bp[3][1], geo)
                    newm = tuple(m + rob for m, rob in zip(newm, robots))
                    newr = rt(robots, 3, 1)
                    new_states.add((newr, newm))
                else:
                    new_states.add((robots, tuple(m + rob for m, rob in zip(material, robots))))
                    if ore >= bp[2][0] and clay >= bp[2][1]:
                        newm = (ore - bp[2][0], clay - bp[2][1], obs, geo)
                        newm = tuple(m + rob for m, rob in zip(newm, robots))
                        newr = rt(robots, 2, 1)
                        new_states.add((newr, newm))
                    if ore >= bp[0]:
                        newm = (ore - bp[0], clay, obs, geo)
                        newm = tuple(m + rob for m, rob in zip(newm, robots))
                        newr = rt(robots, 0, 1)
                        new_states.add((newr, newm))
                    if ore >= bp[1]:
                        newm = (ore - bp[1], clay, obs, geo)
                        newm = tuple(m + rob for m, rob in zip(newm, robots))
                        newr = rt(robots, 1, 1)
                        new_states.add((newr, newm))

            rtime = 32 - t
            sf = lambda n: (n**2+n)/ 2
            sfr = lambda start, end: sf(end) - sf(start - 1)
            obs_per_grob = bp[3][1]
            @functools.cache
            def max_geodes(orobs, grobs, curr_obs, curr_geodes):
                max_obs = sfr(orobs, orobs + rtime - 2) + curr_obs
                max_grobs = max_obs // obs_per_grob + grobs
                return sfr(grobs, max_grobs) + curr_geodes

            # dont ask me why this works, I just gradually reduced how many I pruned until the answer was correct lmao
            states = sorted(new_states, key = lambda s: max_geodes(*s[0][-2:], *s[1][-2:]))[-100000:]

            # best = max(max_geodes(*s[0][-2:], *s[1][-2:]) for s in states)

            # if t == 18:
                # ((2, 3, 2, 1), (4, 10, 2, 0))
                # ((2, 7, 3, 0), (4, 14, 7, 0))
                # print(((2, 7, 3, 0), (4, 14, 7, 0)) in states)
                # print(best)
                # print(next(max_geodes(*s[0][-2:], *s[1][-2:]) for s in states if s == ((2, 7, 3, 0), (4, 14, 7, 0))))
                # pprint(states)
                # print(next(s for s in states if best == max_geodes(*s[0][-2:], *s[1][-2:])))
            # print(t, len(states))
            # states = {s for s in states if max_geodes(*s[0][-2:], *s[1][-2:]) >= best}
            # if t == 18:
            #     print(((2, 7, 3, 0), (4, 14, 7, 0)) in states)
            #     pprint(states)
            #     print(((1, 4, 2, 1), (2, 17, 3, 0)) in states)
            # print(t, len(states))

            # pprint(states)
        quality = max([material[-1] for r, material in states])
        print(quality)
        ans *= quality

    return ans

tests = {
    """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.""" : [33, 3472]
}
#
# test(tests, solve_a, 0)
# a = solve_a()
# print(f"Part 1: {a}\n")
# submit(int(a) if isinstance(a, float) else a, part="a", day=day, year=2022)

# test(tests, solve_b, 1)
b = solve_b()
print(f"Part 2: {b}")
# submit(int(b) if isinstance(b, float) else b, part="b", day=day, year=2022)
#
#
# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")