inp = open(r"..\..\input.txt").read().split("\n")
convData = lambda x:0 if x == "." else 1
initial_state = [convData(i) for i in inp[0][15:]]
rules = [[list(map(convData, rule[:5])), convData(rule[9])] for rule in inp[2:]]

def get_current_state(gens):
    current_state = initial_state
    nullpunkt = 0
    for _ in range(gens):
        last_state = current_state 
        if last_state[:2] != [0,0]:
            last_state = [0,0] + last_state
            nullpunkt += 2
        if last_state[-2:] != [0,0]:
            last_state = last_state + [0,0]
        
        current_state = []
        for i, v in enumerate(last_state):
            if i > 1 and i < len(last_state) - 2:
                adjacent = last_state[i-2:i+3]
            elif i >= len(last_state) - 2:
                adjacent = last_state[i-2:] + [0,0] if len(last_state) - 1 == i else last_state[i-2:] + [0]
            else:
                adjacent = [0,0] + last_state[:i+3]  if i == 0 else [0] + last_state[:i+3]

            for r in rules:
                if adjacent == r[0]:
                    current_state.append(r[1])
                    break
            else:
                current_state.append(0)

    return current_state, nullpunkt

pots, offset = get_current_state(20)
summ = 0
for i,v in enumerate(pots):
    if v != 0:
        summ += i - offset
print(summ)

#My code is getting uglier by the day day D: