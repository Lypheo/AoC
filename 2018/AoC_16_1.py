import itertools, re, copy
raw_data = open(r"input.txt").read().split("\n")
data = []
p_bef = re.compile(r"Before: \[(\d), (\d), (\d), (\d)\]")
p_aft = re.compile(r"After:  \[(\d), (\d), (\d), (\d)\]")
opc = re.compile(r"(\d+) (\d+) (\d+) (\d+)")

for i in itertools.count(start=0, step=4):
    if raw_data[i] == "":
        test_start = i+2
        break
    before = list(map(int, p_bef.match(raw_data[i]).groups()))
    opcode = list(map(int, opc.match(raw_data[i+1]).groups()))
    after = list(map(int, p_aft.match(raw_data[i+2]).groups()))
    data.append({"before":before, "after":after, "opcode":opcode})

test_data = [list(map(int, opc.match(i).groups())) for i in raw_data[test_start:-1]]

def apply(reg, c, new_value):
    out = copy.copy(reg)
    out[c] = new_value
    return out

codes = [lambda reg, a, b, c: apply(reg, c, reg[a] + b),
         lambda reg, a, b, c: apply(reg, c, reg[a] + reg[b]),
         lambda reg, a, b, c: apply(reg, c, reg[a] * reg[b]),
         lambda reg, a, b, c: apply(reg, c, reg[a] * b),
         lambda reg, a, b, c: apply(reg, c, reg[a] & reg[b]),
         lambda reg, a, b, c: apply(reg, c, reg[a] & b),
         lambda reg, a, b, c: apply(reg, c, reg[a] | reg[b]),
         lambda reg, a, b, c: apply(reg, c, reg[a] | b),
         lambda reg, a, b, c: apply(reg, c, reg[a]),
         lambda reg, a, b, c: apply(reg, c, a),
         lambda reg, a, b, c: apply(reg, c, 1 if a > reg[b] else 0),
         lambda reg, a, b, c: apply(reg, c, 1 if reg[a] > b else 0),
         lambda reg, a, b, c: apply(reg, c, 1 if reg[a] > reg[b] else 0),
         lambda reg, a, b, c: apply(reg, c, 1 if a == reg[b] else 0),
         lambda reg, a, b, c: apply(reg, c, 1 if reg[a] == b else 0),
         lambda reg, a, b, c: apply(reg, c, 1 if reg[a] == reg[b] else 0)]

codes_sorted = [None]*16

for sample in data:
    correct_codes = []
    for code in codes:
        if code(sample["before"], sample["opcode"][1], sample["opcode"][2], sample["opcode"][3]) == sample["after"]:
            if code not in codes_sorted:
                correct_codes.append(code)
    if len(correct_codes) == 1:
        codes_sorted[sample["opcode"][0]] = correct_codes[0]

regs = [0,0,0,0]
for i in test_data:
    regs = codes_sorted[i[0]](regs, i[1],i[2],i[3])

print(regs)
