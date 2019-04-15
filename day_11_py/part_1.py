import numpy

serial = 7400
size = 300

def power_level(x, y):
    rack_id = x + 1 + 10
    power = (rack_id * (y + 1) + serial) * rack_id
    power = (power // 100) % 10
    return power - 5

grid = numpy.fromfunction(power_level, (size, size), dtype = int)

# Summed Area Table
sat = grid.cumsum(axis = 0).cumsum(axis = 1)

top_sum = -99
top_coord = []
x = 2
while x < size:
    y = 2
    while y < size:
        if x == 2 and y == 2:
            result = sat[y, x]
        elif y == 2:
            result = sat[y, x] - sat[y, x-3]
        elif x ==  2:
            result = sat[y, x] - sat[y-3, x]
        else:
            result = sat[y, x] + sat[y-3, x-3] - sat[y, x-3] - sat[y-3, x]
        if result > top_sum:
            top_sum = result
            top_coord = [y - 1, x - 1]
        y += 1
    x += 1

print(str(top_coord[0]) + "," + str(top_coord[1]))
