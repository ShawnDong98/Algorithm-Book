def dfs(u):
    if u == n:
        print(' '.join(map(str, path)))
        return
    for i in range(1, n+1):
        if not st[i]:
            st[i] = True
            path.append(i)
            dfs(u + 1)
            path.pop()
            st[i] = False

N = 10
path = []
st = [False] * N

n = int(input())
dfs(0)



