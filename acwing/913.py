N = 100010

n = int(input())
t = list(map(int, input().split()))

t = sorted(t, reverse=True)

res = 0
for i in range(n):
    res += t[i] * i

print(res)
