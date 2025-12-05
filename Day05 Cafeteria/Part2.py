import re

ranges = list()
with open("input.txt", "r") as inf:
    while line := inf.readline().rstrip():
        if match := re.match(r"(\d+)-(\d+)", line):
            ranges.append((int(match[1]), int(match[2])))

combined_ranges = list((ranges.pop(0),))

def find_overlaps(min_val, max_val):
    overlapping_ranges = list()
    for pos, (comb_min, comb_max) in enumerate(combined_ranges):
        if min_val < comb_min < max_val or min_val < comb_max < max_val:
            overlapping_ranges.append(pos)

    return overlapping_ranges


for minimum, maximum in ranges:
    if overlaps := find_overlaps(minimum, maximum):
        for index in overlaps:
            comb_min, comb_max = combined_ranges[index]
            minimum = min(minimum, comb_min)
            maximum = max(maximum, comb_max)
            combined_ranges[index] = (minimum, maximum)
            # do it again for the new combination
            if overlaps := find_overlaps(minimum, maximum):
                for index2 in overlaps:
                    comb_min, comb_max = combined_ranges[index2]
                    combined_ranges[index] = (min(minimum, comb_min), max(maximum, comb_max))

    else:
        combined_ranges.append((minimum, maximum))

total = 0
# turn it into a set to sort and remove duplicates
for minimum, maximum in set(combined_ranges):
    print(f"({minimum},{maximum})")
    total += (maximum-minimum)+1

print (total)