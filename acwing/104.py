N = 100010

n = int(input())
q = list(map(int, input().split()))

q = sorted(q)

res = 0
for i in range(n):
    res += abs(q[i] - q[n//2])

print(res)
