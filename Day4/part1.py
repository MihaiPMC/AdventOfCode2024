f = open("input.txt")

mat = []
for line in f:
    mat.append(list(line.strip()))

cnt = 0
l = len(mat)

for i, row in enumerate(mat):
    for j, char in enumerate(row):
        if char == 'X':
            #vertical
            if i + 3 < l and mat[i + 1][j] == 'M' and mat[i + 2][j] == 'A' and mat[i + 3][j] == 'S':
                cnt += 1
            if i - 3 >= 0 and mat[i - 1][j] == 'M' and mat[i - 2][j] == 'A' and mat[i - 3][j] == 'S':
                cnt += 1
            #horizontal
            if j + 3 < l and mat[i][j + 1] == 'M' and mat[i][j + 2] == 'A' and mat[i][j + 3] == 'S':
                cnt += 1
            if j - 3 >= 0 and mat[i][j - 1] == 'M' and mat[i][j - 2] == 'A' and mat[i][j - 3] == 'S':
                cnt += 1
            #diagonal
            if i + 3 < l and j + 3 < l and mat[i + 1][j + 1] == 'M' and mat[i + 2][j + 2] == 'A' and mat[i + 3][j + 3] == 'S':
                cnt += 1
            if i - 3 >= 0 and j - 3 >= 0 and mat[i - 1][j - 1] == 'M' and mat[i - 2][j - 2] == 'A' and mat[i - 3][j - 3] == 'S':
                cnt += 1
            if i + 3 < l and j - 3 >= 0 and mat[i + 1][j - 1] == 'M' and mat[i + 2][j - 2] == 'A' and mat[i + 3][j - 3] == 'S':
                cnt += 1
            if i - 3 >= 0 and j + 3 < l and mat[i - 1][j + 1] == 'M' and mat[i - 2][j + 2] == 'A' and mat[i - 3][j + 3] == 'S':
                cnt += 1

print(cnt)