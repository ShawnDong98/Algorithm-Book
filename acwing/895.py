N = 1010

a = [0] * N
f = [0] * N

n = int(input())

inp = list(map(int, input().split()))
for i in range(1, n+1):
    a[i] = inp[i-1]

for i in range(1, n+1):
    f[i] = 1
    for j in range(1, i):
        if a[j] < a[i]:
            f[i] = max(f[i], f[j] + 1)


res = 0
for i in range(1, n+1):
    res = max(res, f[i])

print(res)
