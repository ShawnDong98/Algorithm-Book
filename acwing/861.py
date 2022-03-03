def add(a, b):
    global idx
    e[idx] = b
    ne[idx] = h[a]
    h[a] = idx
    idx += 1

def find(x):
    i = h[x]
    while i != -1:
        j = e[i]
        if not st[j]:
            st[j] = True
            if (match[j] == 0 or find(match[j])):
                match[j] = x
                return True
        i = ne[i]

    return False


N = 510
M = 100010
h = [-1] * N
e = [0] * M
ne = [0] * M
idx = 0

match = [0] * N



n1, n2, m = map(int, input().split())

for i in range (m):
    u, v = map(int, input().split())
    add(u, v)

res = 0
for i in range(1, n1+1):
    st = [False] * N
    if find(i): res += 1

print(res)
