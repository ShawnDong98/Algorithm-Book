"""
题目: 输入一个整数数组, 实现一个函数来调整该数组中数字的顺序, 使得所有奇数位于数组的前半部分, 所有偶数位于数组的后半部分。
"""

def condition(num):
    if num % 2 == 0:
        return True
    else: 
        return False

def resort(inp):
    left = 0
    right = len(inp) - 1
    
    while left < right:
        while not condition(inp[left]):
            left += 1
        while condition(inp[right]):
            right -= 1
        if left < right:
            temp = inp[left]
            inp[left] = inp[right]
            inp[right] = temp

    return inp

inp = [1, 2, 3, 4, 5]

print(resort(inp))