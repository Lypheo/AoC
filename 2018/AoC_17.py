import re

inp = open(r"input.txt").read().strip("\n")

data = []
pattern = re.compile(r"(x|y)=(\d+), (x|y)=(\d+)..(\d+)")

for i in inp.split("\n"):
    p = pattern.match(i).groups()
    if p[0] == "x":
        for y in range(int(p[3]), int(p[4])+1):
            data.append((int(p[1]), int(y)))
    else:
        for y in range(int(p[3]), int(p[4])+1):
            data.append((int(y), int(p[1])))

maxY, minY = max(data, key = lambda x: x[1])[1], min(data, key = lambda x: x[1])[1]

wet = set()
occupied = set(data)

def spread(x,y):
    x_r, y_r = x, y
    l_limited, r_limited = False, False
    flow_line = set()
    flow_line.add((x,y))
    while (x,y+1) in occupied:
        if (x-1,y) not in occupied:
            x -= 1
            flow_line.add((x,y))
        else:
            l_limited = True
            break

    while (x_r,y_r+1) in occupied:
        if (x_r+1,y_r) not in occupied:
            x_r += 1
            flow_line.add((x_r,y_r))
        else:
            r_limited = True
            break
    if l_limited and r_limited:
        occupied.update(flow_line)
    if not r_limited:
        flow_down(x_r, y_r)
    if not l_limited:
        flow_down(x, y)
    wet.update(flow_line)

def flow_down(x,y):
    while (x,y+1) not in occupied:
        y += 1
        if not y < minY: wet.add((x,y))
        if y > maxY - 1: return
    spread(x,y)

last = 0
while True:
    flow_down(500, 0)
    if len(occupied) == last:
        break
    last = len(occupied)
    
print(len(wet)) #part 1
print(len(occupied) - len(set(data))) #part 2