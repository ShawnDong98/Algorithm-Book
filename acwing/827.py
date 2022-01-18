# 在节点 k 的右边插入一个数 x
def insert(k, x):
    global idx
    e[idx] = x
    l[idx] = k
    r[idx] = r[i]
    r[k] = idx
    idx += 1

def remove(k):
    l[r[k]] = l[k]
    r[l[k]] = r[k]


N = 100010
e = [0] * N
l = [0] * N
r = [0] * N
idx = 2
m = int(input())

r[0] = 1
l[1] = 0
idx = 2

for i in range(m):
    inp = input().split()
    if inp[0] == 'L':
        x = int(inp[1])
        insert(0, x)
    if inp[0] == 'R':
        x = int(inp[1])
        insert(l[1], x)
    if inp[0] == 'D':
        k = int(inp[1])
        remove(k + 1)
    if inp[0] == 'IL':
        k, x = int(inp[1]), int(inp[2])
        insert(l[k + 1], x)
    if inp[0] == 'IR':
        k, x = int(inp[1]), int(inp[2])
        insert(k + 1, x)

i = r[0]
while i != 1:
    print(e[i], end=' ')
    i = r[i]




