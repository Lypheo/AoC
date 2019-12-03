def solve(inp=open(r"C:\Users\saifu\Downloads\D2P2-RealisticBigBoy", "r").read()[:-1], noun=12, verb=2):
    inp = [int(i) for i in inp.split(",")]
    inp[1:3] = [noun, verb]
    for i in range(0, len(inp), 4):
        opcode = inp[i]
        if opcode == 1:
            inp[inp[i+3]] = inp[inp[i+1]] + inp[inp[i+2]]
        elif opcode == 2:
            inp[inp[i+3]] = inp[inp[i+1]] * inp[inp[i+2]]
        elif opcode == 99:
            break

    return inp[0]

print(f"Part 1: {solve()}")

for noun in range(100):
    for verb in range(100):
        if solve(noun=noun, verb=verb) == 19690720:
            print(f"Part 2: {100 * noun + verb}")
            break