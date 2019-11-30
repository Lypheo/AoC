data = [(line[5], line[36]) for line in open(r"..\..\input.txt")]
requirements = {step:[] for preceding_step, step in data}

for preceding_step, step in data:
	requirements[step].append(preceding_step)

ready = set()
for i in "QWERTZUIOPASDFGHJKLYXCVBNM":
	if (i in [x[0] for x in data]) and (i not in requirements):
		ready.add(i)

finished = set()
in_work = [None]*5
time = 0

while True:
	for i,v in enumerate(in_work):
		if v != None and time - v[1] == ord(v[0]) - 64 + 60:
			finished.add(v[0])
			in_work[i] = None

	for i,v in requirements.items():
		if set(v).issubset(finished) and (not i in finished) and (not i in [x[0] for x in in_work if x != None]):
			ready.add(i)

	for i,v in enumerate(in_work):
		if v == None and len(ready) > 0:
			_next = min(ready)
			ready.remove(_next)
			in_work[i] = [_next, time]

	if len(finished) == len(requirements) + 4:
		break
	time += 1

print(time)