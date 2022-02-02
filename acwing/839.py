def heap_swap(a, b):
    ph[hp[a]], ph[hp[b]] = ph[hp[b]], ph[hp[a]]
    hp[a], hp[b] = hp[b], hp[a]
    h[a], h[b] = h[b], h[a]

def down(u):
    t = u
    if u * 2 <= cnt and h[u * 2] < h[t]: t = u * 2
    if u * 2 + 1 <= cnt and h[u * 2 + 1] < h[t]: t = u * 2 + 1
    if u != t:
        heap_swap(u, t)
        down(t)

def up(u):
    while u // 2 and h[u] < h[u // 2]:
        heap_swap(u, u // 2)
        u >>= 1

n = int(input())
N = 100010

h, ph, hp = [0] * N, [0] * N, [0] * N
cnt = m = 0

for i in range(n):
    inp = input().split()
    if inp[0] == 'I':
        x = int(inp[1])
        cnt += 1
        m += 1
        ph[m], hp[cnt] = cnt, m
        h[cnt] = x
        up(cnt)
    if inp[0] == 'PM':
        print(h[1])
    if inp[0] == 'DM':
        heap_swap(1, cnt)
        cnt -= 1
        down(1)
    if inp[0] == 'D':
        k = int(inp[1])
        k = ph[k]
        heap_swap(k, cnt)
        cnt -= 1
        up(k)
        down(k)
    if inp[0] == 'C':
        k, x = int(inp[1]), int(inp[2])
        k = ph[k]
        h[k] = x
        up(k)
        down(k)


