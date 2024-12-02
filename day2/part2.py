def check(v):
    if sorted(v) != v and sorted(v, reverse=True) != v:
        return False

    ok = True
    for i in range (len(v) - 1):
        if not (1 <= abs(v[i] - v[i + 1]) <= 3):
            ok = False
            break

    if ok:
        return True

f = open("text.in")

ans = 0

for line in f:
    v = list(map(int, line.split()))

    if check(v):
        ans += 1
    else:
        for i in range(len(v)):
            new_v = v[:i] + v[i + 1:]
            if check(new_v):
                ans += 1
                break

print(ans)
