f = open("input.txt")

left = []
right = []
for line in f:
    line = line.split()
    left.append(int(line[0]))
    right.append(int(line[1]))

ans = 0

for i in range(len(left)):
    countOf = right.count(left[i])
    ans += left[i] * countOf

w = open("output", "w")
w.write(str(ans))