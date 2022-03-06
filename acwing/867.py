def divide(x):
    # n 中最多只包含一个大于 sqrt(n) 的质因子， 否则相乘是大于n的
    for k in range(2, int(x**0.5) + 1):
        if x == 1:
            break
        if x % k == 0:
            s = 0
            while x % k == 0:
                x /= k
                s += 1
            print(k, s)
    if x > 1:
        print(int(x), 1)
    print()

n = int(input())

for i in range(n):
    a = int(input())
    divide(a)
