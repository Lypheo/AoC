data = [(line[5], line[36]) for line in open(r"..\..\input.txt")]
requirements = {step:[] for preceding_step, step in data}

for preceding_step, step in data:
	requirements[step].append(preceding_step)

ready = set()
for i in "QWERTZUIOPASDFGHJKLYXCVBNM":
	if (i in [x[0] for x in data]) and (i not in requirements):
		ready.add(i)

finished = set()

out = ""
while True:
	for i,v in requirements.items():
		if set(v).issubset(finished) and not i in finished:
			ready.add(i)
	_next = min(ready)
	finished.add(_next)
	ready.remove(_next)
	out += _next
	if len(finished) == len(requirements) + 4:
		break

print(out)