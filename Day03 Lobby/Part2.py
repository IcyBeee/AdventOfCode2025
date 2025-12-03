sum = 0
no_batteries_required = 12
with (open("input.txt", "r") as inf):
    for batteries in inf.readlines():
        value = 0
        for batteries_remaining in range(no_batteries_required, 0, -1):
            no_batteries_available = len(batteries)
            truncated = batteries[:-batteries_remaining]
            highest = max([int(x) for x in truncated])
            first = batteries.index(str(highest))
            batteries = batteries[first+1:]
            value = (value*10) + highest
        sum += value

print(sum)