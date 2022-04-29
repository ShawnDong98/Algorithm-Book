N = 50010

n = int(input())
cow = []
for i in range(n):
    w, s = map(int, input().split())
    cow.append((w+s, w))

cow = sorted(cow, lambda x: x[0])

res = -2e9
sum = 0
for i in range(n):
    s = cow[i][0] - cow[i][1]
    w = cow[i][1]
    res = max(res, sum - s)
    sum += w

print(res)
