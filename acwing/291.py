N = 12
M = 1 << N

while True:
    f = [[0] * M for _ in range(N)]
    st = [False] * M

    n, m = map(int, input().split())
    if n == 0 and m == 0: break
    for i in range(0, 1<<n):
        cnt = 0
        st[i] = True
        for j in range(0, n):
            if i >> j & 1:
                if (cnt & 1): st[i] = False
                cnt = 0
            else:
                cnt += 1

        if cnt & 1: st[i] = False

    f[0][0] = 1
    for i in range(1, m+1):
        for j in range(0, 1<<n):
            for k in range(0, 1<<n):
                if ((j & k) == 0 and st[j | k]):
                    f[i][j] += f[i-1][k]

    print(f[m][0])


