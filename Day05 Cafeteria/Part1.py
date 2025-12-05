import re

ranges = list()
total = 0

with open("input.txt", "r") as inf:
    while line := inf.readline().rstrip():
        if match := re.match(r"(\d+)-(\d+)", line):
            ranges.append((int(match[1]), int(match[2])))

    while line := inf.readline().rstrip():
        val = int(line)
        for minimum, maximum in ranges:
            if minimum <= val <= maximum:
                total += 1
                break

print(total)