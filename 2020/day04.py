from datetime import datetime
import time
import functools, itertools, collections, re
import numpy as np
from aocd.models import Puzzle
from aocd import submit
import string

day = 4
puzzle = Puzzle(year=2020, day=day)
input_data = puzzle.input_data

def test(tests, solution):
    for i,o in tests.items():
        if (ao := solution(i)) not in o:
            print(f"Testcase failed:\n    Input: {i}\n    Expected output: {o}\n    Actual output: {ao}\n")
            return False
    print(f"Tests successful!")
    return True


def solve_a(inp=input_data):
    pws = (dict(x.split(":") for x in p.split()) for p in inp.split("\n\n"))
    return sum(len(pw.keys()) == 8 or (len(pw) == 7 and "cid" not in pw) for pw in pws)

def solve_b(inp=input_data):
    return sum(
        bool(
                (len(pw.keys()) == 8 or (len(pw.keys()) == 7 and "cid" not in pw))
            and (1920 <= int(pw["byr"]) <= 2002)
            and (2010 <= int(pw["iyr"]) <= 2020)
            and (2020 <= int(pw["eyr"]) <= 2030)
            and ((pw['hgt'].endswith("cm") and 150 <= int(pw['hgt'][:-2]) <= 193) or (pw['hgt'].endswith("in") and 59 <= int(pw['hgt'][:-2]) <= 76))
            and (re.match(r"#[0-9a-f]{6}", pw["hcl"]))
            and (pw["ecl"] in "amb blu brn gry grn hzl oth".split())
            and (re.match(r"^\d{9}$", pw["pid"]))
        )
        for pw in (dict(x.split(":") for x in p.split()) for p in inp.split("\n\n"))
    )

tests = {"""eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719""": (None,4)
}

a = solve_a()
print(f"Part 1: {a}\n")
# test(tests, solve_a)
# submit(a, part="a", day=day, year=2020)

b = solve_b()
if not b:
    exit(0)

print(f"Part 2: {b}")
# test(tests, solve_b)
# submit(b, part="b", day=day, year=2020)

# import time
# t1 = time.time_ns()
# for i in range(times := 1000):
#     solve_b()
# t2 = time.time_ns()
# print(f"Time: {(t2-t1)/(1000000*times)} ms")