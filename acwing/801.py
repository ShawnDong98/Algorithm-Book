n = int(input())
arr = map(int, input().split())
for x in arr:
    s = 0

    i = x
    while i:
        s += 1
        i -= i & -i
    print(s, end=' ')

