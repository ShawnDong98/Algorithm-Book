N = 10

def get(num, l, r):
    res = 0
    for i in range(l, r-1, -1): res = res * 10 + num[i]
    return res

def power10(x):
    res = 1
    while x:
        res *= 10
        x -= 1
    return res

def count(n, x):
    if not n: return 0
    num = []
    while n:
        num.append(n % 10)
        n //= 10
    n = len(num)

    res = 0
    for i in range(n - 1 - (not x), -1, -1):
        if i < n - 1:
            res += get(num, n-1, i+1) * power10(i)
            if not x: res -= power10(i)

        if num[i] == x: res += get(num, i-1, 0) + 1
        elif num[i] > x: res += power10(i)

    return res

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break

    if a > b: a, b = b, a
    for i in range(0, 10):
        print(count(b, i) - count(a-1, i), end=' ')
    print()
