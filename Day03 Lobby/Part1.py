sum = 0
with (open("input.txt", "r") as inf):
    for batteries in inf.readlines():
        first_digit = 0
        first_digit_pos = 0
        for pos in range(len(batteries)-2):
            digit = int(batteries[pos])
            if digit > first_digit:
                first_digit = digit
                first_digit_pos = pos
        second_digit = max([int(x) for x in batteries[first_digit_pos+1:-1]])
        sum += (first_digit*10) + second_digit

print(sum)