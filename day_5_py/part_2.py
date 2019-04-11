from part_1 import change_case

def reduce_length(contents):
    data = contents
    loop = True
    dat_len = len(data)
    hold = data[0]
    count = 1
    while loop:
        if data[count] == change_case(hold):
            data = data[:count - 1] + data[count + 1:]
            dat_len -= 2
            count -= 2
            if count < 0:
                count = 0
            hold = data[count]
            count += 1
            if count >= dat_len:
                loop = False
        else:
            hold = data[count]
            count += 1
            if count >= dat_len:
                loop = False

    return len(data)
    

with open("input.txt", "r") as f:
    data = f.read().strip()

lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
best_letter_to_remove = ""
lowest_length = 50000

for i in range(0, 26):
    new_data = data.replace(lowercase[i], "")
    new_data = new_data.replace(uppercase[i], "")
    if reduce_length(new_data) < lowest_length:
        lowest_length = reduce_length(new_data)
        best_letter_to_remove = uppercase[i]

print(lowest_length)
