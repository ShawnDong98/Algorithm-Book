def insert(x):
    global idx
    k = (x % N + N) % N
    e[idx] = x
    ne[idx] = h[k]
    h[k] = idx
    idx += 1

def find(x):
    k = (x % N + N) % N
    i = h[k]
    while i != -1:
        if e[i] == x: return True
        i = ne[i]
    return False

N = 100003

h = [-1] * N
e = [-1] * N
ne = [-1] * N
idx = 0

n = int(input())

for i in range(n):
    inp = input().split()
    if inp[0] == 'I':
        x = int(inp[1])
        insert(x)
    else:
        x = int(inp[1])
        if find(x): print("Yes")
        else: print("No")
