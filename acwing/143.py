def insert(x):
    global idx
    p = 0
    i = 30
    while i>=0:
        s = x >> i & 1
        if not son[p][s]:
            idx += 1
            son[p][s] = idx
        p = son[p][s]
        i -= 1

def search(x):
    p, res = 0, 0
    i = 30
    while i>=0:
        s = x >> i & 1
        if son[p][s^1]:
            res += 1 << i
            p = son[p][s^1]
        else: p = son[p][s]
        i -= 1
    return res

n = int(input())
arr = list(map(int, input().split()))

N, M = 100010, 3100010
idx = 0
son = [[0] * 2 for _ in range(M)]

for a in arr:
    insert(a)

res = 0
for i in range(n):
    res = max(res, search(arr[i]))

print(res)


