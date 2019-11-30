import re, itertools
fabric = [[0 for i in range(1,1001)] for k in range(1,1001)]

with open("..\\..\\input.txt", "r") as _input:
    two_or_more = 0
    claims = [re.compile(r"#(\d{1,4}) @ (\d{1,3}),(\d{1,3}): (\d{1,3})x(\d{1,3})").match(claim).groups() for claim in [x.strip("\n") for x in list(_input)]]
    for claim in claims:
    	occupied = itertools.product(list(range(int(claim[1]), int(claim[1]) + int(claim[3]))), list(range(int(claim[2]), int(claim[2]) + int(claim[4]))))
    	for i in occupied:
    		fabric[i[0]][i[1]] += 1
    		if fabric[i[0]][i[1]] == 2:
    			two_or_more += 1

    print(two_or_more)
