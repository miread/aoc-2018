with open("input.txt", "r") as f:
    data = f.read().strip()

def change_case(char):
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if char in uppercase:
        return char.lower()
    if char in lowercase:
        return char.upper()

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
    else:
        hold = data[count]
        count += 1
        if count >= dat_len:
            loop = False

print(len(data))
