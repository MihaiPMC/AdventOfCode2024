from collections import defaultdict
from functools import cmp_to_key

f = open("text.in")

firstPart, secondPart = f.read().split("\n\n")

rules = defaultdict(list)
update = []

for line in firstPart.split("\n"):
    a, b = line.split("|")
    rules[int(a)].append(int(b))

for line in secondPart.split("\n"):
    update.append(list(map(int, line.split(","))))

def cmp(a, b):
    if b in rules[a]:
        return -1
    if a in rules[b]:
        return 1
    return 0

ans = 0

for line in update:
    newLine = sorted(line, key = cmp_to_key(cmp))
    if line != newLine:
        ans += newLine[len(newLine) // 2]

print(ans)