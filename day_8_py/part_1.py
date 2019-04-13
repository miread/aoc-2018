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
















#
# print(data)
#
# metadata_sum = 0
#
# def recursive_len(item):
#     if type(item) == list and len(item) == 0:
#         return 0
#     elif type(item) == list:
#         return sum(recursive_len(subitem) for subitem in item)
#     else:
#         return 1
#
# def make_children(data, child_qty):
#     global metadata_sum
#     finished_children = []
#     idx = 0
#     count = 0
#     while count < int(child_qty):
#         if int(data[idx]) > 0:
#             children = make_children(data[idx + 2:], data[idx + 1])
#             node = [[data[idx], data[idx + 1]], children,
#                 data[idx + 2 + recursive_len(children):idx + 2 +
#                     recursive_len(children) + int(data[idx + 1])]]
#             finished_children.append(node)
#             for metadata in node[2]:
#                 metadata_sum += int(metadata)
#             node_len = len(node[0]) + recursive_len(node[1]) + len(node[2])
#             idx += node_len
#         elif int(data[idx]) == 0:
#             node = [[data[idx], data[idx + 1]], [],
#                 data[idx + 2:idx + 2 + int(data[idx + 1])]]
#             finished_children.append(node)
#             for metadata in node[2]:
#                 metadata_sum += int(metadata)
#             node_len = len(node[0]) + len(node[1]) + len(node[2])
#             idx += node_len
#         count += 1
#
#     return finished_children
#
#
# # data = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2".split(" ")
#
# qty_data = int(data[1])
#
# root = [[data[0], data[1]], make_children(data[2:0 - qty_data], data[0]),
#        data[0 - qty_data:]]
#
# for metadata in root[2]:
#     metadata_sum += int(metadata)
#
#
# print(root)
# print(metadata_sum)
