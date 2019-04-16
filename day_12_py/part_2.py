import re

neg_pots = 0

def next_gen(state, dict):
    global neg_pots
    state_len = len(state)
    new_state = ""
    new_state += dict["...." + state[0]]
    new_state += dict["..." + state[0:2]]
    new_state += dict[".." + state[0:3]]
    new_state += dict["." + state[0:4]]
    neg_pots += 2
    count = 0
    while count < state_len - 4:
        new_state += dict[state[count:count + 5]]
        count += 1
    new_state += dict[state[count:count + 5] + "."]
    new_state += dict[state[count + 1:count + 5] + ".."]
    new_state += dict[state[count + 2:count + 5] + "..."]
    new_state += dict[state[count + 3] + "...."]
    for i in range(0, neg_pots):
        if new_state[0] == ".":
            new_state = new_state[1:]
            neg_pots -= 1
    while new_state[-1] == ".":
        new_state = new_state[:-1]
    return new_state

with open("input.txt", "r") as f:
    data = f.readlines()

init = re.match(r"initial state: ([#\.]+)", data[0])
combs = re.compile(r"([\.#]{5}) => (\.|#)")

dict = {}
data_len = len(data)
idx = 2
while idx < data_len:
    result = combs.match(data[idx])
    dict[result.group(1)] = result.group(2)
    idx += 1

print("0:", init.group(1), neg_pots)
plant_pot_sum = 0

next_state = next_gen(init.group(1), dict)
print("1:", next_state, neg_pots)

old_sum = 0
for i in range(2, 159):
    next_state = next_gen(next_state, dict)
    print(str(i) + ":", next_state, neg_pots)
    plant_pot_sum = 0
    for i in range(0, neg_pots):
        if next_state[i] == "#":
            plant_pot_sum += i - neg_pots

    for i in range(neg_pots, len(next_state)):
        if next_state[i] == "#":
            plant_pot_sum += i

    print(plant_pot_sum)
    print(plant_pot_sum, "-", old_sum, "=", plant_pot_sum - old_sum)
    old_sum = plant_pot_sum


print(plant_pot_sum + ((50000000000 - 158) * 86))

# All generations after 158 grow exactly 86 new plants

# At the end of generation 158, we have 16_002 plants

# Next comes 49_999_999_842 generations, each +86 plants
# for a total of 4_929_999_986_412

# Added to the original 16_002, the total should be 4_300_000_002_414
