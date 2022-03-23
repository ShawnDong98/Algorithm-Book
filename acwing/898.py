N = 510
INF = 1e9

n = int(input())
a = [[0] * N for _ in range(N)]
f = [[0] * N for _ in range(N)]

for i in range(1, n+1):
    inp = list(map(int, input().split()))
    for j in range(1, i+1):
        a[i][j] = inp[j-1]

for i in range(n+1):
    for j in range(i+2):
        f[i][j] = -INF

f[1][1]= a[1][1]
for i in range(2, n+1):
    for j in range(1, i+1):
        f[i][j] = max(f[i-1][j-1] + a[i][j], f[i-1][j] + a[i][j])

res = -INF
for i in range(1, n+1): res = max(res, f[n][i])

print(res)


