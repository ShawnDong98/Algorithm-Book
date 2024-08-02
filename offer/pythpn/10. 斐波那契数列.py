"""
题目:

求斐波那契数列的第n项

写一个函数, 输入n, 求斐波那契(Fibonacci)数列的第n项。斐波那契数列的定义如下:

f(0) = 0
f(1) = 1
f(n) = f(n-2) + f(n-1)
"""

def fabornacci(num):
    res = [0, 1]
    if num < 2:
        return res[num]
    
    for i in range(2, num+1):
        res.append(res[i-2] + res[i-1])

    return res[num]


num = int(input())
print(fabornacci(num))