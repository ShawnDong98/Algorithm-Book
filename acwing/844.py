from collections import deque

def bfs():
    q = deque([])
    d[0][0] = 0
    q.append([0, 0])

    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

    while q:
        t = q.popleft()
        for i in range(4):
            x = t[0] + dx[i]
            y = t[1] + dy[i]
            if x >= 0 and x< n and y >= 0 and y < m and g[x][y] == 0 and d[x][y] == -1:
                d[x][y] = d[t[0]][t[1]] + 1
                q.append([x, y])

    return d[n-1][m-1]


n, m = map(int, input().split())

N = 110

d = [[-1] * N for _ in range(N)]

g = []
for i in range(n):
    inp = list(map(int, input().split()))
    g.append(inp)

print(bfs())

