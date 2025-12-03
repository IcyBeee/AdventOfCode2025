sum = 0
no_batteries_required = 12
with (open("input.txt", "r") as inf):
    for batteries in inf.readlines():
        value = 0
        for batteries_remaining in range(no_batteries_required, 0, -1):
            no_batteries_available = len(batteries)
            # The next digit cannot come from the last "batteries_remaining" digits
            truncated_batteries = batteries[:-batteries_remaining]
            highest = max([int(x) for x in truncated_batteries])
            # Find the earliest occurrence of the highest digit
            first_index = batteries.index(str(highest))
            # Strip everything before this digit from the battery list
            batteries = batteries[first_index + 1:]
            value = (value*10) + highest
        sum += value

print(sum)