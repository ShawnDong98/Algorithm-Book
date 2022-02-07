def dfs(u):
    global row, col, dg, udg
    if u == n:
        for i in range(n): print(''.join(g[i]))
        print('')
        return
    for i in range(n):
        if not col[i] and not dg[u+i] and not udg[n-u+i]:
            g[u][i] = 'Q'
            col[i] = dg[u+i] = udg[n-u+i] = 1
            dfs(u+1)
            col[i] = dg[u+i] = udg[n-u+i] = 0
            g[u][i] = '.'
N = 20

n = int(input())

row = [0] * N
col = [0] * N
dg = [0] * N
udg = [0] * N

g = [['.'] * n for _ in range(n)]

dfs(0)
