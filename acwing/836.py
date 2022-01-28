def find(x):
    if p[x] != x: p[x] = find(p[x])
    return p[x]

n, m = map(int, input().split())
p = [i for i in range(0, n+1)]

for i in range(m):
    inp = input().split()
    if inp[0] == 'M':
        a, b = int(inp[1]), int(inp[2])
        p[find(a)] = find(b)
    if inp[0] == 'Q':
        a, b = int(inp[1]), int(inp[2])
        if find(a) == find(b): print("Yes")
        else: print("No")

