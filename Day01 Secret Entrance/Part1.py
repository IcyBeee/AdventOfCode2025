position = 50
zero_count = 0

with open("input.txt", "r") as inf:
    for line in inf.readlines():
        turn = int(line[1:])
        if line[0] == "L":
            turn *= -1

        position = (position + turn) % 100
        if position == 0:
            zero_count += 1

print(zero_count)
