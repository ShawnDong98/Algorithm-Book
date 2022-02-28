def prim():
    global n
    res = 0
    for i in range(n):
        t = -1
        for j in range(1, n+1):
            if not st[j] and (t == -1 or dist[t] > dist[j]):
                t = j

        # 不是第一个点， 并且距离为无穷， 说明不连通
        if i and dist[t] == 0x3f3f3f3f: return 0x3f3f3f3f

        if i: res += dist[t]

        for j in range(1, n+1):
            dist[j] = min(dist[j], g[t][j])

        # 标记该点已进入集合
        st[t] = True

    return res

N = 510
n, m = map(int, input().split())
g = [[0x3f3f3f3f] * N for _ in range(N)]
dist = [0x3f3f3f3f] * N
st = [False] * N

for i in range(m):
    u, v, w = map(int, input().split())
    g[u][v] = g[v][u] = min(g[u][v], w)

t = prim()

if t == 0x3f3f3f3f: print("impossible")
else: print(t)
