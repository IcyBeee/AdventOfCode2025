import re

sum = 0
with open("input.txt", "r") as inf:
    for id_range in  inf.readline().split(","):
        first, last = id_range.split("-")
        for id in range(int(first), int(last)+1):
            idstr = str(id)
            n = 1
            while n <= (len(idstr) // 2):
                if match := re.match(fr"((.){{{n}}})(\1)+$", idstr):
                    # print(f"{idstr} repeating")
                    sum += id
                    break
                n += 1

print(sum)