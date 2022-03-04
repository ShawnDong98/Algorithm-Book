def is_prime(x):
    if x < 2: return False
    i = 2
    # 性质： 如果 d 可以被 n 整除， 那么 n/d 也可以被 n 整除
    while i <= x / i:
        if x % i == 0:
            return False
        i += 1
    return True
n = int(input())
for i in range(n):
    a = int(input())
    if is_prime(a):
        print('Yes')
    else:
        print('No')
