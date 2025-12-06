import re

ranges = list()
with open("input.txt", "r") as inf:
    while line := inf.readline().rstrip():
        if match := re.match(r"(\d+)-(\d+)", line):
            ranges.append([int(match[1]), int(match[2])])

ranges.sort(key=lambda x: x[0])

combined_ranges = list()
minimum, maximum = ranges[0]
for index in range(1, len(ranges)):
    next_min, next_max = ranges[index]
    if next_min <= maximum <= next_max:
        maximum = next_max
    elif next_max > maximum:
        combined_ranges.append((minimum, maximum))
        minimum = next_min
        maximum = next_max
# do the last one
combined_ranges.append((minimum, maximum))

total = 0
for minimum, maximum in combined_ranges:
    total += (maximum-minimum)+1

print (total)