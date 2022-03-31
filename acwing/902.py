N = 1010

n = int(input())
a = ' ' + input()
m = int(input())
b = ' ' + input()
f = [[0] * N for _ in range(N)]

for i in range(m+1): f[0][i] = i
for i in range(n+1): f[i][0] = i

for i in range(1, n+1):
    for j in range(1, m+1):
        f[i][j] = min(f[i-1][j] + 1, f[i][j-1] + 1)
        if a[i] == b[j]: f[i][j] = min(f[i][j], f[i-1][j-1])
        else: f[i][j] = min(f[i][j], f[i-1][j-1] + 1)

print(f[n][m])



