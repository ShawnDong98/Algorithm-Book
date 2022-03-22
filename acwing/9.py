N = 110

n, m = map(int, input().split())
v = [[0] * N for _ in range(N)]
w = [[0] * N for _ in range(N)]
s = [0] * N
f = [0] * N

for i in range(1, n+1):
    s[i] = int(input())
    for j in range(0, s[i]):
        v[i][j], w[i][j] = map(int, input().split())


for i in range(1, n+1):
    for j in range(m, -1, -1):
        for k in range(0, s[i]):
            if v[i][k] <= j:
                f[j] = max(f[j], f[j-v[i][k]] + w[i][k])

print(f[m])
