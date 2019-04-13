idx = 0

with open("input.txt", "r") as f:
    data = f.read().replace("\n", "").split(" ")

def scroller():
    global idx
    value = data[idx]
    idx += 1
    return value

def read_nodes():
    num_children = scroller()
    num_metadata = scroller()
    children = [read_nodes() for x in range(0, int(num_children))]
    metadata = [scroller() for x in range(0, int(num_metadata))]
    return [num_children, num_metadata, children, metadata]

def sum_node(node):
    if len(node[2]) > 0:
        total_sum = 0
        for entry in node[3]:
            if int(entry) <= len(node[2]) and int(entry) != 0:
                total_sum += sum_node(node[2][int(entry) - 1])
    else:
        total_sum = 0
        for entry in node[3]:
            total_sum += int(entry)
    return total_sum

result = read_nodes()

print(sum_node(result))
