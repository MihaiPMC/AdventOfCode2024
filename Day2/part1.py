f = open("text.in")

ans = 0

for line in f:
    v = list(map(int, line.split()))
    if sorted(v) != v and sorted(v, reverse=True) != v:
        continue

    ok = True
    for i in range (len(v) - 1):
        if not (1 <= abs(v[i] - v[i + 1]) <= 3):
            ok = False
            break

    if ok:
        ans += 1

print(ans)
