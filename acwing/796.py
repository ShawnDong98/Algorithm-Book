n, m, q = map(int, input().split())
matrix = [[0] * (m + 1)]
for i in range(n):
    arr = [0] + list(map(int, input().split()))
    matrix.append(arr)


S = matrix
for i in range(1, n + 1):
    for j in range(1, m + 1):
        S[i][j] += S[i-1][j] + S[i][j-1] - S[i-1][j-1]


for i in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    print(S[x2][y2] - S[x1-1][y2] - S[x2][y1-1] + S[x1 - 1][y1 - 1])

