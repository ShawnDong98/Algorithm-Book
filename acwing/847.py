from collections import deque
def add(a, b):
    global idx
    e[idx] = b
    ne[idx] = h[a]
    h[a] = idx
    idx += 1

def bfs():
    q = deque([1])
    d[1] = 0

    while q:
        t = q.popleft()
        i = h[t]
        while i != -1:
            j = e[i]
            if d[j] == -1:
                d[j] = d[t] + 1
                q.append(j)
            i = ne[i]

    return d[n]

N = 100010
h = [-1] * N
e = [0] * N
ne = [0] * N
idx = 0
d = [-1] * N

n, m = map(int, input.split())

for i in range(m):
    a, b  = map(int, input.split())
    add(a, b)

print(bfs())
