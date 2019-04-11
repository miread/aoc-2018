with open("input.txt", "r") as f:
    data = f.readlines()
    for line in data:
        count = 1
        while count < 250:
            misses, checker, bad_spot = 0, 0, 0
            while checker < 26:
                if line[checker] != data[count][checker]:
                    misses += 1
                    bad_spot = checker
                checker += 1
            if misses == 1:
                print(line[:bad_spot] + line[bad_spot + 1:])
            count += 1
