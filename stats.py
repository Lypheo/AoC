import json, time
import datetime
from pprint import pprint

import requests, os

YEAR = 2021
day = min([datetime.datetime.today().day, 25])
# uri = 'https://adventofcode.com/{year}/leaderboard/private/view/134143.json'.format(year=YEAR) # weebautism
# uri = 'https://adventofcode.com/2021/leaderboard/private/view/993406.json'.format(year=YEAR) # aocg
uri = 'https://adventofcode.com/{year}/leaderboard/private/view/963655.json'.format(year=YEAR) # SSC
response = requests.get(uri, cookies={'session': os.environ["AOC_SESSION"]})
data = response.text

lb = json.loads(data)["members"]
timings = {}
def unix_to_ts(t, day):
    t6am = datetime.datetime(YEAR, 12, day, 6, tzinfo=datetime.timezone(datetime.timedelta(hours=1)))
    unix6am = time.mktime(t6am.timetuple())
    return time.strftime('%H:%M:%S', time.gmtime(t - unix6am))

anons = {
    "652077": "Frechdachs",
    "668767": "kaitokid",
    "405237": "Nala_Alan",
    "386138": "MolesterMan"
}
alias = {
    "Eschryn" : "zCore",
    "cuanim" : "Vardë",
    "daf276" : "Attila",
    "Krieger381" : "Arranun"
}

dead = ["kaitokid", "ll-FP-ll"]

for k, v in lb.items():
    times = {k: sorted([unix_to_ts(i["get_star_ts"], int(k)) for i in v.values()]) for k, v in v["completion_day_level"].items()}
    rname = v["name"] or anons.get(v["id"], "Anon " + v["id"])
    name = alias.get(rname, rname)
    # if name in dead: continue
    timings[name] = times

for d in range(1, day+1):
    print(f"Day {d:02d}:")
    participants = sorted({k: v[str(d)] for k,v in timings.items() if str(d) in v}.items(), key=lambda k: k[1][1] if len(k[1]) > 1 else "99:99:99")#[:10]
    c = 1
    for p, t in participants:
        print(str(c).rjust(3, " ") + ": {} {}   {}".format(p.ljust(20), t[0], t[1] if len(t) > 1 else "-"))
        c += 1


