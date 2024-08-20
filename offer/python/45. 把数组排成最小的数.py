"""
题目： 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如，输入数组 {3, 32, 321}，则打印出这 3 个数字能排成的最小数字 321323。
"""
from itertools import permutations

def func(nums):
    res = []
    for perm in permutations(nums):
        res.append(int("".join(map(str, perm))))
    
    return min(res)



nums = [3, 32, 321]
print(func(nums))