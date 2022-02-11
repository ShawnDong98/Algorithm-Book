def add(a, b):
    global idx
    e[idx] = b
    ne[idx] = h[a]
    h[a] = idx
    idx += 1

def dfs(u):
    global res
    st[u] = True

    size, sum = 0, 0
    i = h[u]
    while i != -1:
        j = e[i]
        if st[j]:
            i = ne[i]
            continue

        s = dfs(j)
        size = max(size, s)
        sum += s

        i = ne[i]
    size = max(size, n - sum - 1)
    res = min(res, size)

    return sum + 1

N = 100010
M = N * 2
h = [-1] * N
e, ne = [0] * M, [0] * M
idx = 0
res = N
st = [False] * N

n = int(input())


for i in range(n-1):
    a, b = map(int, input().split())
    add(a, b)
    add(b, a)

dfs(1)

print(res)
