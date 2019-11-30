_input = open("..\\input.txt", "r")
current_freq = 0
freqs = []
seen_freqs = set([0])

for i in _input:
	freqs.append(int(i.strip("\n")))

def find_duplicate():
	while True:
		for i in freqs:
			global current_freq
			current_freq += i
			size = len(seen_freqs)
			seen_freqs.add(current_freq)
			if size == len(seen_freqs):
				return current_freq

print(sum(freqs)) #1
print(find_duplicate(), len(seen_freqs)) #2
