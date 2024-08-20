"""
题目: 我们把只包含因子2 3和5的数称作丑数 求按从小到大的顺序的第1500个丑数 

例如6 8都是丑数 但14不是 因为它包含因子7 习惯上我们把1当作第一个丑数
"""

def is_ugly_number(num):
    while num % 2 == 0:
        num //= 2
    while num % 3 == 0:
        num //= 3
    while num % 5 == 0:
        num //= 5

    if num == 1:
        return True
    else:
        return False
    

def GetUglyNumber(index):
    if index <= 0:
        return 0
    
    number = 0
    uglyFound = 0
    while uglyFound < index:
        number += 1
        
        if is_ugly_number(number):
            uglyFound += 1

    
    return number


print(GetUglyNumber(1500))