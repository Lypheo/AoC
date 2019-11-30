IDs = []
with open("..\\input.txt", "r") as _input:
	for ID in _input:
		IDs.append(ID.strip("\n"))

twos = 0
threes = 0

for ID in IDs:
	seen = set()
	ID_1 = ID

	for i in range(1, len(ID)+1):	
		if ID[0] not in seen:
			seen.add(ID[0])
			ID = ID[1:]
		else:
			ID = ID[1:] + ID[0]

	has_two, has_three = False, False

	for i in set(ID):
		if ID_1.count(i) == 3:
			has_three = True
		if ID_1.count(i) == 2:
			has_two = True

	if has_two:
		twos += 1
	if has_three:
		threes += 1

print(twos*threes)
