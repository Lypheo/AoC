import functools, itertools, collections, re
from aocd.models import Puzzle

day = 19
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

def solve(inp=input_data):
    def dist(p1, p2):
        return sum(abs(a-b) for a,b in zip(p1,p2))

    def orientations(ip):
        for p in itertools.permutations(ip):
            for signs in itertools.product([1,-1], [1,-1], [1,-1]):
                px = tuple([p[i]*signs[i] for i in range(3)])
                yield px

    scanners = [(i, [tuple(int(c) for c in b.split(",")) for b in sc.split("\n")[1:]])  for i, sc in enumerate(inp.split("\n\n"))]
    pos = {}
    oris = {}
    ds = []
    for i,s in scanners:
        ds.append({b1: set(dist(b1, p) for p in s if p != b1) for b1 in s})

    for (i1, s1), (i2, s2) in itertools.permutations(scanners, 2):
        seenboth = set()
        for b1, b2 in itertools.product(s1, s2):
            overlap = ds[i2][b2] & ds[i1][b1]
            if len(overlap) >= 11:
                seenboth.add((b1, b2))
        if not seenboth:
            continue
        a,b = seenboth.pop()
        c,d = seenboth.pop()
        for id, (bo, do) in enumerate(zip(orientations(b), orientations(d))):
            s2loc1 = tuple(ac-bc for ac,bc in zip(a,bo))
            s2loc2 = tuple(ac-bc for ac,bc in zip(c,do))
            if s2loc1 == s2loc2:
                break
        oris[(i1, i2)] = id
        pos[(i1, i2)] = s2loc2

    beacons = set(scanners[0][1])
    import networkx as nx

    paths = {}
    G = nx.Graph()
    G.add_edges_from(oris.keys())
    for i in range(1,len(scanners)):
        paths[(0, i)] = path = nx.shortest_path(G, 0, i)
        spos = pos[(0, path[1])]
        last = [0]
        for s, t in itertools.pairwise(path[1:]):
            last.append(s)
            to = pos[(s,t)]
            for v,w in reversed(list(itertools.pairwise(last))):
                to = list(orientations(to))[oris[(v,w)]]

            spos = tuple(ac+bc for ac,bc in zip(spos,to))
        pos[(0, i)] = spos

    def lor(p):
        return list(orientations(p))

    def transform(scid, point):
        path = paths[(0, scid)]
        for v,w in reversed(list(itertools.pairwise(path))):
            po = lor(point)[oris[(v,w)]]
            origin = pos[(v,w)]
            point = tuple(ac+bc for ac,bc in zip(origin,po))
        return point

    for i, sc in scanners[1:]:
        for point in sc:
            beacons.add(transform(i, point))

    spos = [v for k,v in pos.items() if k[0] == 0] + [(0,0,0)]
    return len(beacons), max(dist(p1, p2) for p1, p2 in itertools.permutations(spos, 2))


tests = {
#     """--- scanner 1 ---
# 686,422,578
# 605,423,415
# 515,917,-361
# -336,658,858
# 95,138,22
# -476,619,847
# -340,-569,-846
# 567,-361,727
# -460,603,-452
# 669,-402,600
# 729,430,532
# -500,-761,534
# -322,571,750
# -466,-666,-811
# -429,-592,574
# -355,545,-477
# 703,-491,-529
# -328,-685,520
# 413,935,-424
# -391,539,-444
# 586,-435,557
# -364,-763,-893
# 807,-499,-711
# 755,-354,-619
# 553,889,-390
#
# --- scanner 4 ---
# 727,592,562
# -293,-554,779
# 441,611,-461
# -714,465,-776
# -743,427,-804
# -660,-479,-426
# 832,-632,460
# 927,-485,-438
# 408,393,-506
# 466,436,-512
# 110,16,151
# -258,-428,682
# -393,719,612
# -211,-452,876
# 808,-476,-593
# -575,615,604
# -485,667,467
# -680,325,-822
# -627,-443,-432
# 872,-547,-609
# 833,512,582
# 807,604,487
# 839,-516,451
# 891,-625,532
# -652,-548,-490
# 30,-46,-14""" : [-1,-1,],
    """--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14""" : [79, 3621]
}

# test(tests, solve_a, 0)
# a = solve_a()
# print(f"Part 1: {a}\n")
# submit(int(a) if isinstance(a, float) else a, part="a", day=day, year=2021)

test(tests, lambda t: solve(t)[1], 1)
test(tests, lambda t: solve(t)[0], 0)
# b = solve_b()
# if b:
#     print(f"Part 2: {b}")
    # submit(int(b) if isinstance(b, float) else b, part="b", day=day, year=2021)
#
#
import time
t1 = time.time_ns()
for i in range(times := 30):
    solve()
t2 = time.time_ns()
print(f"Time: {(t2-t1)/(1000000*times)} ms")