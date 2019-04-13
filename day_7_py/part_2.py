import re

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Worker():
    def __init__(self):
        self.task = "."
        self.timer = 0

def check_reqs(reqs, completed, started):
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if letter not in completed and letter not in started:
            if letter not in reqs:
                return letter
            else:
                ready = True
                for req in reqs[letter]:
                    if req not in completed:
                        ready = False
                if ready == True:
                    return letter
    return "."

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

worker_1 = Worker()
worker_2 = Worker()
worker_3 = Worker()
worker_4 = Worker()
worker_5 = Worker()
worker_list = [worker_1, worker_2, worker_3, worker_4, worker_5]

step_times = {alphabet[i]: 61 + i for i in range(0,26)}
step_times["."] = 0

completed = ""
started = ""
clock = 0

# print(step_times)

while len(completed) < 26:
    to_be_completed = ""
    un_started = ""
    for worker in worker_list:
        if worker.task == ".":
            check = check_reqs(reqs, completed, started)
            worker.task = check
            worker.timer = step_times[check]
            if worker.task != ".":
                started += check
        if worker.timer > 0:
            worker.timer -= 1
        if worker.timer == 0 and worker.task != ".":
            to_be_completed += worker.task
            un_started += worker.task
            worker.task = "."
    completed += to_be_completed
    for item in un_started:
        started.replace(item, "")
    clock += 1

print(clock)
