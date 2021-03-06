idx = 0
meta_sum = 0

with open("input.txt", "r") as f:
    data = f.read().replace("\n", "").split(" ")

def scroller():
    global idx
    value = data[idx]
    idx += 1
    return value

def read_nodes():
    global meta_sum
    num_children = scroller()
    num_metadata = scroller()
    children = [read_nodes() for x in range(0, int(num_children))]
    metadata = [scroller() for x in range(0, int(num_metadata))]
    for item in metadata:
        meta_sum += int(item)
    return [num_children, num_metadata, children, metadata]

print(read_nodes())
print(meta_sum)
