import itertools, re, copy
_input = "540561"
score_sequence = list(map(int, _input))
recipes = [3,7,1,0]
elf1 = 0
elf2 = 1
while True:
    summ = recipes[elf1] + recipes[elf2]
    if summ > 9:
        recipes.extend([1, summ % 10])
    else:
        recipes.append(summ)

    elf1 = ((elf1 + recipes[elf1]+1) % (len(recipes)))
    elf2 = ((elf2 + recipes[elf2]+1) % (len(recipes)))
    if _input in ''.join(str(i) for i in recipes):
        break 

print(''.join(str(i) for i in recipes).index(_input))
