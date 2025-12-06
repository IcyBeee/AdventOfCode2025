import operator
from functools import reduce

problems = list()

with open("input.txt", "r") as inf:
    lines = inf.readlines()
    operations = lines.pop().split()
    for line in lines:
        problems.append([int(x) for x in line.split()])

total = 0
for problem_no in range(len(problems[0])):
    values = [row[problem_no] for row in problems]
    if operations[problem_no] == "*":
        total += reduce(operator.mul, values, 1)
    elif operations[problem_no] == "+":
        total += reduce(operator.add, values, 0)

print(total)