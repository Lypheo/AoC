import re, itertools, copy
_days = [0,0,31,59,90,120,151,181,212,243,273,304,334]
with open("..\\..\\input.txt", "r") as _input:
    data = [x.strip("\n") for x in _input]
    sorted_data = []
    for i in data:
        p = re.compile(r"\[(\d{4})\-(\d{2})\-(\d{2}) (\d{2}):(\d{2})\] Guard #(\d+) begins shift").match(i)
        if p:
            p = p.groups()
            line = {"years":p[0], "months":p[1], "days":p[2], "h":p[3], "m":p[4], "nr":p[5]}
        else:
            p = re.compile(r"\[(\d{4})\-(\d{2})\-(\d{2}) (\d{2}):(\d{2})\] (\w{1})").match(i).groups()
            line = {"years":p[0], "months":p[1], "days":p[2], "h":p[3], "m":p[4]}
        line = {k:int(v) for k,v in line.items()}
        line["time"] = (_days[line["months"]] + line["days"]) * 24 * 60 + line["h"] * 60 + line["m"]
        sorted_data.append(line)
    sorted_data.sort(key=lambda x:x["time"])

    guards = {i["nr"]:[] for i in sorted_data if "nr" in i }
    
    current_id = 0
    sleeping = False
    last = None
    for k,i in enumerate(sorted_data):
        if "nr" in i:
            current_id = i["nr"]
        elif not sleeping:
            sleeping = True
            last = copy.copy(i)
        else:
            guards[current_id].extend(list(range(last["m"],i["m"]))) 
            sleeping = False

    sleepiest = max(guards, key=lambda x:len(guards[x]))
    sleepiest_minute = max(set(guards[sleepiest]), key=guards[sleepiest].count)
    
    _data = [(i, v.count(max(set(v), key=v.count)), max(set(v), key=v.count)) for i,v in guards.items() if v != []]
    print(max(_data, key=lambda x:x[1])[0]*max(_data, key=lambda x:x[1])[2])
