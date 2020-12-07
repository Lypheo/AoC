import json, time
import datetime
from pprint import pprint

import requests, os

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0"
YEAR = 2020
day = datetime.datetime.today().day
# uri = 'https://adventofcode.com/{year}/leaderboard/private/view/134143.json'.format(year=YEAR) # weebautism
uri = 'https://adventofcode.com/2020/leaderboard/private/view/198336.json'.format(year=YEAR) # aocg
response = requests.get(uri, cookies={'session': os.environ["AOC_SESSION"]}, headers={'User-Agent': USER_AGENT})
data = response.text

lb = json.loads(data)["members"]

timings = {}
def unix_to_ts(t, day):
    t6am = datetime.datetime(YEAR, 12, day, 6, tzinfo=datetime.timezone(datetime.timedelta(hours=1)))
    unix6am = time.mktime(t6am.timetuple())
    return time.strftime('%H:%M:%S', time.gmtime(t - unix6am))

anons = {
    "668767": "kaitokid",
    "652077": "Frechdachs",
    "405237": "Nala_Alan (?)",
    "386138": "MolesterMan"
}

for k, v in lb.items():
    times = {k: sorted([unix_to_ts(int(i["get_star_ts"]), int(k)) for i in v.values()]) for k, v in v["completion_day_level"].items()}
    timings[v["name"] or (anons[v["id"]] if v["id"] in anons else "Anon " + v["id"])] = times

for d in range(1, day+1):
    print(f"Day {d:02d}:")
    participants = sorted({k: v[str(d)] for k,v in timings.items() if str(d) in v}.items(), key=lambda k: k[1][1] if len(k[1]) > 1 else "99:99:99")#[:10]
    c = 1
    for p, t in participants:
        print(str(c).rjust(3, " ") + ": {} {}   {}".format(p.ljust(20), t[0], t[1] if len(t) > 1 else "-"))
        c += 1


