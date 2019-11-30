IDs = list(map(lambda x:list(x), open("..\\input.txt", "r").read().split("\n")))

def is_similiar(x,y):
	diff = 0
	for i in range(0,26):
		if x[i] != y[i]:
			diff += 1
	return True if diff == 1 else False

for i,ID in enumerate(IDs):
	for k in range(i+1, 250):
		if is_similiar(ID, IDs[k]):
			print("".join(ID), "".join(IDs[k]))
