from collections import namedtuple

def bellman_ford():
    global k, m
    dist[1] = 0
    for i in range(k):
        last = dist.copy()
        for j in range(m):
            e = edges[j]
            dist[e.b] = min(dist[e.b], last[e.a] + e.c)




N, M = 510, 10010
edge = namedtuple('edge', 'a, b, c')
edges = []
dist = [0x3f3f3f3f] * N
last = [0x3f3f3f3f] * N


n, m, k = map(int, input().split())

for i in range(m):
    x, y, z = map(int, input().split())
    edges.append(edge(x, y, z))

bellman_ford()
if dist[n] > 0x3f3f3f3f / 2: print('impossible')
else: print(dist[n])




