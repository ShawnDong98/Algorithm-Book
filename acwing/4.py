N = 110

n, m = map(int, input().split())
v = [0] * N
w = [0] * N
s = [0] * N
f = [[0] * N for _ in range(N)]

for i in range(1, n+1):
    v[i], w[i], s[i] = map(int, input().split())
    for i in range(1, n+1):
        for j in range(0, m+1):
            k = 0
            while k <= s[i] and k * v[i] <= j:
                f[i][j] = max(f[i][j], f[i-1][j-k*v[i]] + k*w[i])
                k += 1

print(f[n][m])

