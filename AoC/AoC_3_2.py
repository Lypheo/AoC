import re
from itertools import product
fabric = [[0 for i in range(1,1001)] for k in range(1,1001)]

with open("..\\..\\input.txt", "r") as _input:
    claims = [list(map(int,re.compile(r"#(\d{1,4}) @ (\d{1,3}),(\d{1,3}): (\d{1,3})x(\d{1,3})").match(claim).groups())) for claim in [x.strip("\n") for x in list(_input)]]
    for claim in claims:
    	occupied = product(list(range(claim[1], claim[1] + int(claim[3]))), list(range(claim[2], claim[2] + claim[4])))
    	for i in occupied:
    		fabric[i[0]][i[1]] += 1

    for claim in claims:
    	occupied = list(product(list(range(claim[1], claim[1] + int(claim[3]))), list(range(claim[2], claim[2] + claim[4]))))
    	if sum([fabric[i[0]][i[1]] for i in occupied]) == len(occupied):
    		print(claim[0])

#holy shit, this is so laughably bad :notlikemiya:
