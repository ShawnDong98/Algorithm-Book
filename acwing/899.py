def edit_distance(a, b):
    la = len(a) - 1
    lb = len(b) - 1

    for i in range(lb + 1): f[0][i] = i
    for i in range(la + 1): f[i][0] = i

    for i in range(1, la + 1):
        for j in range(1, lb + 1):
            f[i][j] = min(f[i-1][j] + 1, f[i][j-1] + 1)
            f[i][j] = min(f[i][j], f[i-1][j-1] + (a[i] != b[j]))

    return f[la][lb]

N = 15
M = 1010
n, m = map(int, input().split())
f = [[0] * N for _ in range(N)]
str_ = []

for i in range(n):
    inp = ' ' + input()
    str_.append(inp)

for _ in range(m):
    inp = input().split()
    s = ' ' + inp[0]
    limit = int(inp[1])

    res = 0
    for i in range(n):
        if edit_distance(str_[i], s) <= limit:
            res += 1

    print(res)


