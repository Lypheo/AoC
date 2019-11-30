from collections import defaultdict
players = 455; marbles = 7122300
circle = [0]
cmi = 0 #current marble index
scores = defaultdict(int)

for i in range(1,marbles+1):
	if i % 23 == 0:
		cmi = cmi - 7 if cmi > 6 else len(circle) + cmi - 7
		scores[i % players] += i + circle.pop(cmi)
		continue
	cmi = cmi + 2 if len(circle) - 1 != cmi else 1
	circle.insert(cmi, i)
	if i % 10000 == 0:
		print(i, " of ", marbles, ". Progress: ", i/marbles)

print(max(scores.values()))