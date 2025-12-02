position = 50
last_position = 50
zero_count = 0

with open("input.txt", "r") as inf:
    for line in inf.readlines():
        turn = int(line[1:])
        if abs(turn) > 100:
            zero_count += (abs(turn) // 100)
            turn = turn % 100
        if line[0] == "L":
            turn *= -1

        position = position + turn
        if last_position != 0:
            if position <= 0 or position > 99:
                zero_count += 1
        position = position % 100
        last_position = position

print(zero_count)
