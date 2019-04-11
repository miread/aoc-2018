import re

with open("input.txt", "r") as f:
    data = f.readlines()
    fabric = [[] for c in range(0, 1100)]
    for i in range(0, 1100):
        fabric[i] = [0 for x in range(0, 1100)]

    prog = re.compile(
        r"(#\d+\s@\s)(?P<start_x>\d+)(,)(?P<start_y>\d+)(:\s)(?P<size_x>\d+)(x)(?P<size_y>\d+)"
        )

    for line in data:
        result = prog.match(line)
        for i in range(0, int(result.group('size_y'))):
            for j in range(0, int(result.group('size_x'))):
                fabric[int(result.group('start_y')) + i][int(result.group('start_x')) + j] += 1

    output = 0
    for row in fabric:
        for num in row:
            if num > 1:
                output += 1
    print(output)
