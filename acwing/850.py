from heapq import heappush, heappop

def add(a, b, c):
    global idx
    e[idx] = b
    w[idx] = c
    ne[idx] = h[a]
    h[a] = idx
    idx += 1
def dijkstra():
    dist[1] = 0
    heap = []
    heappush(heap, (0, 1))

    while heap:
        t = heappop(heap)

        ver, distance = t[1], t[0]

        if st[ver]: continue
        st[ver] = True

        i = h[ver]
        while i != -1:
            j = e[i]
            if dist[j] > dist[ver] + w[i]:
                dist[j] = dist[ver] + w[i]
                heappush(heap, (dist[j], j))
            i = ne[i]
    if dist[n] == 0x3f3f3f3f: return -1
    return dist[n]

N = 1000010
h = [-1] * N
e = [0] * N
ne = [0] * N
idx = 0
w = [0] * N
dist = [0x3f3f3f3f] * N
st = [False] * N

n, m = map(int, input().split())

for i in range(m):
    x, y, z = map(int, input().split())
    add(x, y, z)

print(dijkstra())
