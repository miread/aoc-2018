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
top_window = 0

window = 1
while window < 25:
    x = window - 1
    while x < size:
        y = window - 1
        while y < size:
            if x == window - 1 and y == window - 1:
                result = sat[y, x]
            elif y == window - 1:
                result = sat[y, x] - sat[y, x - window]
            elif x ==  window - 1:
                result = sat[y, x] - sat[y - window, x]
            else:
                result = (sat[y, x] + sat[y - window, x - window]
                         - sat[y, x - window] - sat[y - window, x])
            if result > top_sum:
                top_sum = result
                top_coord = [y - window + 2, x - window + 2]
                top_window = window
            y += 1
        x += 1
    window += 1

print(str(top_coord[0]) + "," + str(top_coord[1]) + "," + str(top_window))
