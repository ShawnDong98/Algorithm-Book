n = int(input())
p = ' ' + input()
m = int(input())
s = ' ' + input()

N = 100010
M = 1000010

ne = [0] * N

i, j = 2, 0
while i <= n:
    while (j and p[i] != p[j+1]): j = ne[j]
    if (p[i] == p[j+1]): j += 1
    ne[i] = j
    i += 1

i, j = 1, 0
while i <= m:
    while (j and s[i] != p[j + 1]): j = ne[j]
    if(s[i] == p[j+1]): j += 1
    if(j == n):
        print(i-n, end=' ')
        j = ne[j]
    i += 1
