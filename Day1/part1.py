f = open("input.txt")

left = []
right = []
for line in f:
    line = line.split()
    left.append(line[0])
    right.append(line[1])

ans = 0
left = sorted(left)
right = sorted(right)

for i in range(len(left)):
    ans += abs(int(left[i]) - int(right[i]))

w = open("output", "w")
w.write(str(ans))