N = 310
n = int(input())
s = [0] + list(map(int, input().split()))
f = [[0] * (N) for _ in range(N)]

for i in range(n+1): s[i] += s[i-1]

for l in range(2, n+1):
    i = 1
    while i + l - 1 <= n:
        left = i
        right = i + l -1
        f[left][right] = 1e8
        for k in range(left, right):
            f[left][right] = min(f[left][right], f[left][k] + f[k+1][right] + s[right] - s[left-1])
        i += 1
print(f[1][n])
