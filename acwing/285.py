import sys
sys.setrecursionlimit(1000000)

def add(a, b):
    global idx
    e[idx] = b
    ne[idx] = h[a]
    h[a] = idx
    idx += 1

def dfs(u):
    f[u][1] = happy[u]

    i = h[u]
    while i != -1:
        j = e[i]
        dfs(j)
        f[u][1] += f[j][0]
        f[u][0] += max(f[j][0], f[j][1])
        i = ne[i]

N = 6010

h = [-1] * N
e = [0] * N
ne = [0] * N
idx = 0

happy = [0] * N
f = [[0] * 2 for _ in range(N)]
has_fa = [False] * N

n = int(input())
for i in range(1, n+1):
    happy[i] = int(input())

for i in range(n-1):
    a, b = map(int, input().split())
    add(b, a)
    has_fa[a] = True

root = 1
while has_fa[root]: root += 1

dfs(root)

print(max(f[root][0], f[root][1]))
