import re

with open("input.txt", "r") as f:
    data = f.readlines()

reqs = {}

for line in data:
    result = re.match(
        r"Step (?P<req>[A-Z])[a-z ]+(?P<step>[A-Z])[a-z ]+.",
        line)
    if result.group("step") in reqs:
        reqs[result.group("step")].append(result.group("req"))
    else:
        reqs[result.group("step")] = [result.group("req")]

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
completed = ""
while len(completed) < 26:
    count = 0
    while count < 26:
        if alphabet[count] not in completed:
            if alphabet[count] not in reqs:
                completed += alphabet[count]
                count = -1
            else:
                ready = True
                for req in reqs[alphabet[count]]:
                    if req not in completed:
                        ready = False
                if ready == True:
                    completed += alphabet[count]
                    count = -1
        count += 1

print(completed)
