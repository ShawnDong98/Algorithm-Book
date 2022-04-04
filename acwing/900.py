N = 1010
mod = 1e9 + 7

f = [0] * N

n = int(input())
f[0] = 1
for i in range(1, n+1):
    for j in range(i, n+1):
        f[j] = (f[j] + f[j-i]) % mod

print(int(f[n]))
