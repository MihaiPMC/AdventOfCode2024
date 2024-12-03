import re

f = open("input.txt")

s = f.read()

match = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", s)

ans = 0
ok = True

for m in match:
    if m == "do()":
        ok = True
    elif m == "don't()":
        ok = False
    elif ok:
        m = m[4:-1].split(",")
        print(m)
        ans += int(m[0]) * int(m[1])

print (ans)