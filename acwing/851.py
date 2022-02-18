from collections import deque

def add(a, b, c):
    global idx
    e[idx] = b
    w[idx] = c
    ne[idx] = h[a]
    h[a] = idx
    idx += 1


def spfa():
    dist[1] = 0
    q = deque([1])
    st[1] = True

    while q:
        t = q.popleft()
        st[t] = False

        i = h[t]
        while i != -1:
            j = e[i]
            if dist[j] > dist[t] + w[i]:
                dist[j] = dist[t] + w[i]
                if not st[j]:
                    st[j] = True
                    q.append(j)
            i = ne[i]

    return dist[n]


N = 100010
h = [-1] * N
w = [0] * N
e = [0] * N
ne = [0] * N
idx = 0

dist = [0x3f3f3f3f] * N
st = [False] * N


n, m = map(int, input().split())

for i in range(m):
    x, y, z = map(int, input().split())
    add(x, y, z)

t = spfa()
if t == 0x3f3f3f3f: print("impossible")
else: print(t)


