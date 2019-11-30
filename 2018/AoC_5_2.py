import re

with open(r"..\..\input.txt", "r") as _input:
    lengths = []
    polymer_org = _input.read()
    for i in "abcdefghijklmnopqrstuvwxyz":
        polymer = re.sub("[{}{}]".format(i, i.upper()),"", polymer_org)
        reacted = ""
        while polymer != "":
            reacted += polymer[0]
            polymer = polymer[1:]
            while polymer and reacted:
                if reacted[-1] == polymer[0].swapcase():
                    reacted = reacted[:-1]
                    polymer = polymer[1:]
                else:
                    break
        lengths.append(len(reacted))
    print(min(lengths))