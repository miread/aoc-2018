with open("input.txt", "r") as f:
    data = f.readlines()

dat_len = len(data)
count = 0
while count < dat_len:
    data[count] = str(count + 1) + ", " + data[count]
    count += 1

with open("input_with_id.txt", "w") as f:
    f.writelines(data)

with open("input_with_id.txt", "r") as f:
    data = f.readlines()

highest_x, lowest_x = 0, 500
highest_y, lowest_y = 0, 500

for line in data:
    id, x, y = line.replace("\n", "").split(", ")
    if int(x) > highest_x:
        highest_x = int(x)
    if int(y) > highest_y:
        highest_y = int(y)
    if int(x) < lowest_x:
        lowest_x = int(x)
    if int(y) < lowest_y:
        lowest_y = int(y)
x_len = highest_x - lowest_x
y_len = highest_y - lowest_y
grid = [[0 for i in range(0, x_len)] for j in range(0, y_len)]

count = 0
while count < y_len:
    inner_count = 0
    while inner_count < x_len:
        closest_point = []
        lowest_distance = 500
        for point in data:
            id, x, y = point.replace("\n", "").split(", ")
            x = int(x) - lowest_x
            y = int(y) - lowest_y
            x_distance = abs(x - inner_count)
            y_distance = abs(y - count)
            taxicab_distance = x_distance + y_distance
            if taxicab_distance < lowest_distance:
                closest_point = [id]
                lowest_distance = taxicab_distance
            if taxicab_distance == lowest_distance and id not in closest_point:
                closest_point.append(id)

        if len(closest_point) > 1:
            grid[count][inner_count] = "x"
        else:
            grid[count][inner_count] = closest_point[0]
        inner_count += 1
    count += 1

dict = {str(x): 0 for x in range(1, 51)}
dict["x"] = 0
count = 0
while count < y_len:
    inner_count = 0
    while inner_count < x_len:
        dict[grid[count][inner_count]] += 1
        inner_count += 1
    count += 1

blacklist = ["x"]
for point in grid[0]:
    if point not in blacklist:
        blacklist.append(point)
for point in grid[-1]:
    if point not in blacklist:
        blacklist.append(point)
for row in grid:
    if row[0] not in blacklist:
        blacklist.append(row[0])
    if row[-1] not in blacklist:
        blacklist.append(row[-1])



highest_output = 0
for key, value in dict.items():
    if key not in blacklist and value > highest_output:
        highest_output = value

print(highest_output)

print(blacklist)
