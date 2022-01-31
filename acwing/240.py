def find(x):
    if p[x] != x:
        t = find(p[x]);
        d[x] += d[p[x]]
        p[x] = t

    return p[x]

n, k = map(int, input().split())
N = 50010
p, d = [0] * N, [0] * N
res = 0
for i in range(1, n+1):
    p[i] = i

for i in range(k):
    t, x, y = map(int, input().split())
    if x > n or y > n: res += 1
    else:
        px, py = find(x), find(y)
        if t == 1:
            if px == py and (d[x] - d[y]) % 3: res += 1
            elif px != py:
                p[px] = py
                d[px] = d[y] - d[x]
        if t == 2:
            if px == py and (d[x] - d[y] - 1) % 3: res += 1
            elif px != py:
                p[px] = py
                d[px] = d[y] + 1 - d[x]

print(res)
