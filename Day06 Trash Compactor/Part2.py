import operator
from functools import reduce

problems = list()
total = 0
with open("input.txt", "r") as inf:
    lines = inf.readlines()
    values = list()
    for col in reversed(range(len(lines[0]))):
        num = 0
        op = None
        for row in range(len(lines)):
            val = lines[row][col]
            if val.isdigit():
                num = (num*10) + int(val)
            elif val == "+":
                op = operator.add
            elif val == "*":
                op = operator.mul
        if num > 0:
            values.append(num)
        if op:
            total += reduce(op, values)
            values.clear()

print(total)