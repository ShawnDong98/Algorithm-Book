from collections import deque

def add(a, b):
    global idx
    e[idx] = b
    ne[idx] = h[a]
    h[a] = idx
    idx += 1

def dfs(u, c):
    color[u] = c
    i = h[u]
    while i != -1:
        j = e[i]
        if not color[j]:
            # 3 - c 的结果要么是1, 要么是2 
            if not dfs(j, 3-c): return False
        elif color[j] == c:
            return False
        i = ne[i]

    return True

def bfs(u, c):
    queue = deque([u])
    color[u] = c
    while queue:
        cur = queue.popleft()
        cur_color = color[cur]
        i = h[cur]
        while i != -1:
            j = e[i]
            if not color[j]:
                color[j] = 3 - cur_color
                queue.append(j)
            elif color[j] == cur_color:
                return False
            i = ne[i]
    return True

N = 100010
M = 200010
h = [-1] * N
e = [0] * M
ne = [0] * M
idx = 0

color = [0] * N
n, m = map(int, input().split())

for i in range(m):
    u, v = map(int, input().split())
    add(u, v)
    add(v, u)

flag = True

for i in range(1, n + 1):
    if not color[i]:
        if not bfs(i, 1):
            flag = False
            break

if flag: print("Yes")
else: print("No")
