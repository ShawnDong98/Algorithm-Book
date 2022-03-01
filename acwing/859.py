from collections import namedtuple

def find(x):
    if p[x] != x: p[x] = find(p[x])
    return p[x]

def kruskal():
    global edges, n, p
    edges = sorted(edges, key=lambda edge: edge.w)
    
    for i in range(1, n+1): p[i] = i
    
    res = 0
    cnt = 0
    for i in range(m):
        u, v, w = edges[i].u, edges[i].v, edges[i].w
        u = find(u)
        v = find(v)

        if u != v:
            p[u] = v
            res += w
            cnt += 1

    if cnt < n - 1: return 0x3f3f3f3f
    return res




N = 100010
M = 200010

n, m = map(int, input().split())
p = [10] * N

edge = namedtuple('edge', 'u, v, w')
edges = [edge(-1, -1, float('inf'))] * M

for i in range(m):
    u, v, w = map(int, input().split())
    edges[i] = edge(u, v, w)



t = kruskal()

if t == 0x3f3f3f3f: print("impossible")
else: print(t)
