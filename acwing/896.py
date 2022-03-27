N = 100010

n = int(input())
a = [0] * N
q = [0] * N

inp = list(map(int, input().split()))
for i in range(n):
    a[i] = inp[i]

lens = 0
for i in range(n):
    l = 0
    r = lens
    while l < r:
        mid = l + r + 1 >> 1
        if q[mid] < a[i]: l = mid
        else: r = mid - 1
    lens = max(lens, r + 1)
    q[r + 1] = a[i]

print(lens)

