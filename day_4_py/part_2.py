import re

with open("sorted_input.txt", "r") as f:
    data = f.readlines()

nap_list = {}
current_guard = ""

for line in data:
    result = re.match(
        r"\[\d+-\d+-\d+ \d+:(?P<time>\d+)\] (?P<action>.+)", line
        )
    if (result.group("action") != "falls asleep"
        and result.group("action") != "wakes up"):
        guard_start = re.match(
            r"Guard #(?P<num>\d+) begins shift",
            result.group("action")
            )
        current_guard = guard_start.group("num")

    if result.group("action") == "falls asleep":
        if current_guard in nap_list:
            nap_list[current_guard] += " " + result.group("time")
        else:
            nap_list[current_guard] = result.group("time")

    if result.group("action") == "wakes up":
        nap_list[current_guard] += " " + result.group("time")

final_list = {}
for guard, times in nap_list.items():
    minutes = {x: 0 for x in range(0, 60)}

    checker = "stopped"
    counter = 0

    for time in times.split(" "):
        if checker == "stopped":
            checker = "started"
            minutes[int(time)] += 1
            counter = int(time) + 1
        else:
            while counter < int(time):
                minutes[counter] += 1
                counter += 1
            checker = "stopped"
    final_list[guard] = minutes

highest_nap_count = 0
best_guard = ""
best_minute = ""
for guard, minute_list in final_list.items():
    for minute, nap_count in minute_list.items():
        if nap_count > highest_nap_count:
            highest_nap_count = nap_count
            best_guard = guard
            best_minute = minute

print(int(best_guard) * int(best_minute))
