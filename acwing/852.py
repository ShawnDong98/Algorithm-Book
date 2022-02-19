from collections import deque

def add(a, b, c):
    global idx
    e[idx] = b
    w[idx] = c
    ne[idx] = h[a]
    h[a] = idx
    idx += 1

def spfa():
    q = deque([])
    for i in range(1, n+1):
        st[i] = True
        q.append(i)

    while q:
        t = q.popleft()

        st[t] = False

        i = h[t]
        while i != -1:
            j = e[i]
            if dist[j] > dist[t] + w[i]:
                dist[j] = dist[t] + w[i]
                cnt[j] = cnt[t] + 1

                if cnt[j] >= n: return True
                if not st[j]:
                    st[j] = True
                    q.append(j)
            i = ne[i]
    return False


N = 10010
h = [-1] * N
w = [0] * N
e = [0] * N
ne = [0] * N
idx = 0

dist = [0x3f3f3f3f] * N
cnt = [0] * N
st = [False] * N

n, m = map(int, input().split())

for i in range(m):
    x, y, z = map(int, input().split())
    add(x, y, z)

if spfa(): print("Yes")
else: print("No")

