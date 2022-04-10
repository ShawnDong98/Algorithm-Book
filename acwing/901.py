def dp(x, y):
    if f[x][y] != -1: return f[x][y]

    f[x][y] = 1
    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]
        if a >= 1 and a <= R and b >= 1 and b <= C and g[x][y] > g[a][b]:
            f[x][y] = max(f[x][y], dp(a, b) + 1)

    return f[x][y]

N = 310
g = [[0] * N for _ in range(N)]
f = [[-1] * N for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

R, C = map(int, input().split())

for i in range(1, R+1):
    inp = list(map(int, input().split()))
    for j in range(1, C+1):
        g[i][j] = inp[j-1]

res = 0
for i in range(1, R+1):
    for j in range(1, C+1):
        res = max(res, dp(i,j))

print(res)
