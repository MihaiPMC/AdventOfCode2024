f = open("text.in")

file = f.read().split("\n")

rules = {}
update = []
ans = 0

mRules = {}

for line in file:
    if '|' in line:
        a, b = map(int, line.split("|"))
        if b not in rules:
            rules[b] = []
        rules[b].append(a)
    elif line.strip() == "":
        continue
    else:
        update.append(list(map(int, line.split(","))))

print (update)
print (rules)

for line in update:
    currentList = []
    ok = True
    for number in line:
        if number not in rules:
            currentList.append(number)
        else:
            currentList.append(number)
            for prev in rules[number]:

                if prev in line and prev not in currentList:
                    print(line, number, prev)
                    ok = False
                    break
        if not ok:
            break
    if ok:
        ans += line[len(line) // 2]
print(ans)




