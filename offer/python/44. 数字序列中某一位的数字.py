"""
题目： 数字以 0123456789101112131415⋯ 的格式序列化到一个字符序列中。在这个序列中, 第 5 位（从 0 开始计数）是 5, 第 13 位是 1, 第 19 位是 4, 等等。请写一个函数, 求任意第 n 位对应的数字。
"""

def func(n):
    current_num = 0
    str_ = ""

    while len(str_) <= n:
        str_ += str(current_num)
        current_num += 1

    return str_[n]


print(func(5))
print(func(13))
print(func(19))