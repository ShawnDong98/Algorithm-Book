n = int(input())
q = list(map(int, input().split()))
s = [0] * 100010
res = 0
i = j = 0

while i < n:
    s[q[i]] += 1
    while j < i and s[q[i]] > 1:
        s[q[j]] -= 1
        j += 1
    res = max(res, i - j + 1)
    i += 1

print(res)
