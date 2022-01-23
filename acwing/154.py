n, k = map(int, input().split())
a = list(map(int, input().split()))

N = 1000010
q = [0] * N

hh, tt = 0, -1
i = 0
while i < n:
    if hh <= tt and i - k + 1 > q[hh]:
        hh += 1
    while hh <= tt and a[q[tt]] >= a[i]:
        tt -= 1
    tt += 1
    q[tt] = i
    if i >= k - 1: print(a[q[hh]], end=' ')
    i += 1

print('')
hh, tt = 0, -1
i = 0
while i < n:
    if hh <= tt and i - k + 1 > q[hh]:
        hh += 1
    while hh <= tt and a[q[tt]] <= a[i]:
        tt -= 1
    tt += 1
    q[tt] = i

    if i >= k - 1: print(a[q[hh]], end=' ')
    i += 1

