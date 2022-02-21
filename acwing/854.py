def floyd():
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

N = 210
d = [[0] * N for _ in range(N)]

n, m, k = map(int, input().split())

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j: d[i][j] = 0
        else: d[i][j] = float('inf')

for i in range(m):
    x, y, z = map(int, input().split())
    d[x][y] = min(d[x][y], z)

floyd()

for _ in range(k):
    x, y = map(int, input().split())
    t = d[x][y]
    if t >= float('inf'): print('impossible')
    else: print(t)
