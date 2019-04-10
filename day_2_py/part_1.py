from collections import Counter

with open("input.txt", "r") as f:
    data = f.readlines()
    double_count, triple_count = 0, 0
    for line in data:
        line.replace("\n", "")
        counter = Counter(line)
        doubles = [k for k in counter if counter[k] == 2]
        triples = [k for k in counter if counter[k] == 3]
        if len(doubles) > 0:
            double_count += 1
        if len(triples) > 0:
            triple_count += 1
    print(double_count * triple_count)
