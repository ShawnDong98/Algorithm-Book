N = 12010
M = 2010

n, m = map(int, input().split())
v = [0] * N
w = [0] * N
f = [0] * M

cnt = 0
for i in range(1, n + 1):
    a, b, s = map(int, input().split())
    k = 1
    while k <= s:
        cnt += 1
        v[cnt] = a * k
        w[cnt] = b * k
        s -= k
        k *= 2
    if s > 0:
        cnt += 1
        v[cnt] = a * s
        w[cnt] = b * s

n = cnt

for i in range(1, n + 1):
    j = m
    while j >= v[i]:
        f[j] = max(f[j], f[j - v[i]] + w[i])
        j -= 1

print(f[m])


