"""
RSA加密算法在网络安全世界中无处不在, 它利用了极大整数因数分解的困难度, 数据越大, 安全系数越高, 给定一个32位正整数, 请对其进行因数分解, 找出是哪两个素数的乘积。

输入描述

一个正整数num, 0 < num <= 2147483647

输出描述

如果成功找到, 以单个空格分割, 从小到大输出两个素数, 分解失败, 请输出-1, -1

用例

| 输入 | 15 |
| --- | --- |
| 输出 | 3 5 |

| 输入 | 27 |
| --- | --- |
| 输出 | -1 -1 |
"""


def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0: 
            return False
    return True

def func(num):
    for i in range(1, int(num**0.5)+1):
        if is_prime(i):
            temp = num // i
            if is_prime(temp):
                if temp * i == num:
                    return i, temp
                
    return -1, -1


num = int(input())

t1, t2 = func(num)
print(f"{t1} {t2}")