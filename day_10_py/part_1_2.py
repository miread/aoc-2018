import re

with open("input.txt", "r") as f:
    data = f.readlines()


def check_highest(list, coord):
    output = -99999
    if coord == "x":
        for point in list:
            if int(point[0]) > output:
                output = int(point[0])
        return output
    if coord == "y":
        for point in list:
            if int(point[1]) > output:
                output = int(point[1])
        return output

def check_lowest(list, coord):
    output = 99999
    if coord == "x":
        for point in list:
            if point[0] < output:
                output = point[0]
        return output
    if coord == "y":
        for point in list:
            if point[1] < output:
                output = point[1]
        return output

def move_points(list):
    return [[x[0] + x[2], x[1] + x[3], x[2], x[3]] for x in list]


data = [line.replace("\n", "") for line in data]

match = re.compile(r"\w+=< ?(-?\d+), *(-?\d+)> \w+=< ?(-?\d+), *(-?\d+)>")

data = [[int(match.match(x).group(1)), int(match.match(x).group(2)),
        int(match.match(x).group(3)), int(match.match(x).group(4))] for x in data if
        match.match(x) != None]

timer = 0
x_range = 9999999
y_range = 9999999
while True:
    new_data = move_points(data)
    bottom_x = check_lowest(new_data, "x")
    top_x = check_highest(new_data, "x")
    bottom_y = check_lowest(new_data, "y")
    top_y = check_highest(new_data, "y")
    new_x_range = abs(top_x - bottom_x)
    new_y_range = abs(top_y - bottom_y)
    if new_x_range < x_range or new_y_range < y_range:  # Good move
        timer += 1
        data = new_data
        x_range = new_x_range
        y_range = new_y_range
    else:
        break

img = ["." * (x_range + 1) for _ in range(0, y_range + 1)]

for point in data:
    bottom_x = check_lowest(data, "x")
    bottom_y = check_lowest(data, "y")
    x = point[0] - bottom_x
    y = point[1] - bottom_y
    img[y] = img[y][:x] + "#" + img[y][x + 1:]

for line in img:
    print(line)

print(timer, "seconds elapsed")
