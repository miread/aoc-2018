import re

with open("input.txt", "r") as f:
    data = f.readlines()

with open("sorted_input.txt", "w") as f:
    f.writelines(sorted(data))

with open("sorted_input.txt", "r") as f:
    data = f.readlines()

guard_list = {}
nap_list = {}
current_guard = ""
sleep_start = 0

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
        sleep_start = int(result.group("time"))
        if current_guard in nap_list:
            nap_list[current_guard] += " " + result.group("time")
        else:
            nap_list[current_guard] = result.group("time")

    if result.group("action") == "wakes up":
        if current_guard in guard_list:
            guard_list[current_guard] += int(result.group("time")) - sleep_start
        else:
            guard_list[current_guard] = int(result.group("time")) - sleep_start
        nap_list[current_guard] += " " + result.group("time")

most_sleep = 0
sleepiest_guard = ""

for guard, sleep_time in guard_list.items():
    if sleep_time > most_sleep:
        most_sleep = sleep_time
        sleepiest_guard = guard

minutes = {x: 0 for x in range(1, 60)}

checker = "stopped"
counter = 0
for time in nap_list[sleepiest_guard].split(" "):
    if checker == "stopped":
        checker = "started"
        minutes[int(time)] += 1
        counter = int(time) + 1
    else:
        while counter < int(time):
            minutes[counter] += 1
            counter += 1
        checker = "stopped"

best_minute = ""
num_naps = 0
for minute, naps in minutes.items():
    if naps > num_naps:
        num_naps = naps
        best_minute = minute

print(int(sleepiest_guard) * int(best_minute))
