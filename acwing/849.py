def dijkstra():
    global n
    dist[1] = 0

    for i in range(n-1):
        t = -1
        for j in range(1, n+1):
            if not st[j] and (t == -1 or dist[t] > dist[j]):
                t = j

        for j in range(1, n+1):
            dist[j] = min(dist[j], dist[t] + g[t][j])

        st[t] = True
    if dist[n] == 0x3f3f3f3f: return -1
    return dist[n]

N = 510
g = [[0x3f3f3f3f] * N for _ in range(N)]
dist = [0x3f3f3f3f] * N
st = [False] * N

n, m = map(int, input().split())

for i in range(m):
    x, y, z = map(int, input().split())
    g[x][y] = min(g[x][y], z)

print(dijkstra())
