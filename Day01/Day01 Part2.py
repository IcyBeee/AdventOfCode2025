position = 50
zero_count = 0

with open("input.txt", "r") as inf:
    for line in inf.readlines():
        turn = int(line[1:])
        if line[0] == "L":
            turn *= -1

        position = position + turn
        if position <= 0 or position > 99:
            zero_count += abs(int(turn / 100)) + 1
        position = position % 100

print(zero_count)
