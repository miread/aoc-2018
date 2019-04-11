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
        total_distance = 0
        for point in data:
            id, x, y = point.replace("\n", "").split(", ")
            x = int(x) - lowest_x  # Offset x, y to match grid
            y = int(y) - lowest_y
            x_distance = abs(x - inner_count)
            y_distance = abs(y - count)
            taxicab_distance = x_distance + y_distance
            total_distance += taxicab_distance

        if total_distance < 10000:
            grid[count][inner_count] = 1
        inner_count += 1
    count += 1

area = 0
count = 0
while count < y_len:
    inner_count = 0
    while inner_count < x_len:
        if grid[count][inner_count] == 1:
            area += 1
        inner_count += 1
    count += 1

print(area)
