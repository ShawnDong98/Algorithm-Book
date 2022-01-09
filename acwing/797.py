def insert(b, l, r, c):
    b[l] += c
    b[r+1] -= c
    

n, m = map(int, input().split())
nums = [0] + list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

b = [0 for _ in range(n + 2)]

for i in range(1, n+1):
    insert(b, i, i, nums[i])
for query in queries:
    insert(b, *query)

res = [0] * (n+1)
for i in range(1, n+1):
    res[i] = res[i-1] + b[i]

print(' '.join(map(str, res[1:])))