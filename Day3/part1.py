import re

f = open("input.txt")

s = f.read()

match = re.findall(r"mul\((\d+),(\d+)\)", s)

ans = 0
for m in match:
    ans += int(m[0]) * int(m[1])

print(ans)