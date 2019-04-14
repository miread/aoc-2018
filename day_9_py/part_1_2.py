import re
from collections import deque

data_pt1 = "458 players; last marble is worth 72019 points"
data_pt2 = "458 players; last marble is worth 7201900 points"

result = re.match(r"(?P<players>\d+)[a-z ;]+(?P<end>\d+)[a-z ]+", data_pt2)

scores = {x: 0 for x in range(1, int(result.group("players")) + 1)}

board = deque([0])
turn = 1
count = 1

while count <= int(result.group("end")):
    if count % 23 > 0:
        board.rotate(-1)
        board.append(count)
    else:
        board.rotate(7)
        scores[turn] += count + board[-1]
        board.pop()
        board.rotate(-1)

    count += 1
    turn += 1
    if turn not in scores.keys():
        turn = 1

winning_score = 0
for score in scores.values():
    if score > winning_score:
        winning_score = score
print(winning_score)
