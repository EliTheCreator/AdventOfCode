import os
import re
import time
import datetime


def main():
    file = open("input", "r")
    lines = sorted([x for x in file])
    file.close()

    guards_total_mins = {}
    guards_total_per_min = {}
    current_guard = 0
    prev_timestmp: int
    for line in lines:
        f, s, fw, sw, *_ = line.split()

        timestmp = int(time.mktime(datetime.datetime.strptime(
            "1970" + (f + " " + s)[5:-1], "%Y-%m-%d %H:%M").timetuple()) / 60)

        if fw == "Guard":
            current_guard = int(sw[1:])
            if not guards_total_per_min.keys().__contains__(current_guard):
                guards_total_per_min[current_guard] = [0 for x in range(60)]
                guards_total_mins[current_guard] = 0
        elif fw == "wakes":
            startat = prev_timestmp % 60
            duration = timestmp-prev_timestmp

            guards_total_mins[current_guard] += duration

            for x in range(duration):
                guards_total_per_min[current_guard][(startat+x) % 60] += 1

        prev_timestmp = timestmp

    guard_id: int
    times = 0
    day: int
    for guard in guards_total_mins.keys():
        max_min_key = max(range(len(
            guards_total_per_min[guard])), key=guards_total_per_min[guard].__getitem__)
        if guards_total_per_min[guard][max_min_key] > times:
            times = guards_total_per_min[guard][max_min_key]
            day = max_min_key
            guard_id = guard

    print(guard_id * day)


main()
