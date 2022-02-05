def get(l, r):
    return (h[r] - h[l-1] * p[r - l + 1]) % mod
N, P, mod = 100010, 131, 2**64
h, p = [0] * N, [0] * N

n, m = map(int, input().split())
string = ' ' + input().strip()

p[0] = 1
for i in range(1, n+1):
    h[i] = (h[i-1] * P + ord(string[i])) % mod
    p[i] = (p[i-1] * P) % mod
for i in range(m):
    l1, r1, l2, r2 = map(int, input().split())
    if get(l1, r1) == get(l2, r2): print("Yes")
    else: print("No")

