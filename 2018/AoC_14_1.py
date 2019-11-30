import itertools, re, copy
_input = 540561
recipes = [3,7,1,0]
elf1 = 0
elf2 = 1
while len(recipes) < _input + 10:
    summ = recipes[elf1] + recipes[elf2]
    if summ > 9:
        recipes.extend([1, summ % 10])
    else:
        recipes.append(summ)

    elf1 = ((elf1 + recipes[elf1]+1) % (len(recipes)))
    elf2 = ((elf2 + recipes[elf2]+1) % (len(recipes)))

print("".join(str(i) for i in recipes[_input:_input+10]))