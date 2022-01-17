def add_to_head(x):
    global idx, head
    e[idx] = x
    ne[idx] = head
    head = idx
    idx += 1

def add(k, x):
    global idx
    e[idx] = x
    ne[idx] = ne[k]
    ne[k] = idx
    idx += 1

def remove(k):
    ne[k] = ne[ne[k]]


N = 100010
n = int(input())

e = [0] * N
ne = [0] * N
idx = 0
head = -1

for i in range(n):
    op = input().split()
    if op[0] == 'H':
        add_to_head(int(op[1]))
    elif op[0] == 'I':
        add(int(op[1]) - 1, int(op[2]))
    else:
        k = int(op[1])
        if k:
            remove(k - 1)
        else:
            head = ne[head]

i = head
res = []
while i != -1:
    res.append(e[i])
    i = ne[i]

print(' '.join(map(str, res)))
