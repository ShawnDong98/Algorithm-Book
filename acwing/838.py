def down(u):
    t = u
    if u * 2 <= cnt and h[u * 2] < h[t]: t = u * 2
    if u * 2 + 1 <= cnt and h[u * 2 + 1] < h[t]: t = u * 2 + 1
    if u != t:
        tmp = h[t]
        h[t] = h[u]
        h[u] = tmp
        down(t)

n, m = map(int, input().split())
N = 100010
h = [0] + list(map(int, input().split()))
cnt = n

i = int(n / 2)
while i:
    down(i)
    i -= 1

while m:
    print(h[1], end=' ')
    h[1] = h[cnt]
    cnt -= 1
    down(1)
    m -= 1


