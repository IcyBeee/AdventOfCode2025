sum = 0
with open("input.txt", "r") as inf:
    for id_range in  inf.readline().split(","):
        first, last = id_range.split("-")
        for id in range(int(first), int(last)+1):
            idstr = str(id)
            if idstr[:len(idstr)//2] == idstr[len(idstr)//2:]:
                print(f"{id} - duplicates")
                sum += int(id)

print(sum)