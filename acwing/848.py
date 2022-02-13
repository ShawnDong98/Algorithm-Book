def add(a, b):
    global idx
    e[idx] = b
    ne[idx] = h[a]
    h[a] = idx
    idx += 1

def topsort():
    hh, tt = 0, -1

    for i in range(1, n+1):
        if not d[i]:
            tt += 1
            q[tt] = i
    while hh <= tt:
        t = q[hh]
        hh += 1

        i = h[t]
        while i != -1:
            j = e[i]
            d[j] -= 1
            if d[j] == 0:
                tt += 1
                q[tt] = j
            i = ne[i]
    return tt == n-1

N = 100010
h = [-1] * N
e = [0] * N
ne = [0] * N
d = [0] * N
q = [0] * N
idx = 0

n, m = map(int, input().split())

for i in range(m):
    x, y = map(int, input().split())
    add(x, y)
    d[y] += 1

if not topsort(): print("-1")
else: print(' '.join(map(str, q[:n])))

