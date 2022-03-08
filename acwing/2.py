N = 1010
v = [0] * N
w = [0] * N
f = [0] * N

n, m = map(int, input().split())

for i in range(1, n+1):
    v[i], w[i] = map(int, input().split())

for i in range(1, n+1):
    for j in range(m, v[i]-1, -1):
        f[j] = max(f[j], f[j-v[i]] + w[i])

print(f[m])

