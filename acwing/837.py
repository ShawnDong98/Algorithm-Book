def find(x):
    if p[x] != x: p[x] = find(p[x])
    return p[x]

n, m = map(int, input().split())
N = 100010
p = [0] * N
cnt = [0] * N

for i in range(1, n+1):
    p[i] = i
    cnt[i] = 1

for i in range(m):
    inp = input().split()
    if inp[0] == 'C':
        a, b = int(inp[1]), int(inp[2])
        a, b = find(a), find(b)
        if a != b:
            p[a] = b
            cnt[b] += cnt[a]
    if inp[0] == 'Q1':
        a, b = int(inp[1]), int(inp[2])
        if find(a) == find(b): print("Yes")
        else: print('No')
    if inp[0] == 'Q2':
        a = int(inp[1])
        print(cnt[find(a)])
