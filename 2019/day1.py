input_data = open("bigboyinput", "r").read()[:-1]

def solve(inp=input_data):
    def get_fuel(mass):
        fuel = mass // 3 - 2
        return 0 if fuel < 1 else fuel + get_fuel(fuel)

    masses = [int(i) // 3 - 2 for i in inp.split("\n")]
    part1 = sum(masses)
    return part1, sum(get_fuel(mass) for mass in masses) + part1

a, b = solve()
print(f"Part 1: {a}")
print(f"Part 2: {b}")