def find(x):
    t = (x % N + N) % N
    while h[t] != null and h[t] != x:
        t += 1
        if t == N: t = 0
    return t
N, null = 200003, 0x3f3f3f3f
h = [0x3f3f3f3f] * N

n = int(input())

for i in range(n):
    inp = input().split()
    if inp[0] == 'I':
        x = int(inp[1])
        h[find(x)] = x
    else:
        x = int(inp[1])
        if(h[find(x)] == null): print("No")
        else: print("Yes")



