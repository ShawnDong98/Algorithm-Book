N = 20
M = 1 << 20

w = []
f = [[0x3f3f3f3f] * N for _ in range(M)]

n = int(input())
for i in range(0, n):
    inp = list(map(int, input().split()))
    w.append(inp)

f[1][0] = 0
for i in range(0, 1 << n):
    for j in range(0, n):
        if i >> j & 1:
            for k in range(n):
                if i >> k & 1:
                    f[i][j] = min(f[i][j], f[i-(1<<j)][k] + w[k][j])


print(f[(1<<n)-1][n-1])
