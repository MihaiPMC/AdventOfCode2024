f = open("input.txt")

mat = []
for line in f:
    mat.append(list(line.strip()))

cnt = 0
l = len(mat)

for i, row in enumerate(mat):
    for j, char in enumerate(row):
        if char == 'A' and 0 < i < l - 1 and 0 < j < l - 1:
            if mat[i - 1][j - 1] == 'M' and mat[i + 1][j + 1] == 'S' or mat[i - 1][j - 1] == 'S' and mat[i + 1][j + 1] == 'M':
                if mat[i - 1][j + 1] == 'M' and mat[i + 1][j - 1] == 'S' or mat[i - 1][j + 1] == 'S' and mat[i + 1][j - 1] == 'M':
                    cnt += 1



print(cnt)