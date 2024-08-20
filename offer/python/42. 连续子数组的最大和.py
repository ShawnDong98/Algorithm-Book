"""
题目：输入一个整型数组 数组里有正数也有负数 数组中的一个或连续多个整数组成一个子数组 求所有子数组的和的最大值 要求时间复杂度为 O(n)
"""

def func(inp):
    res = []
    for start in range(0, len(inp)-1):
        for end in range(start+1, len(inp)):
            res.append(sum(inp[start:end]))

    return max(res)

def max_sub_array(nums):
    max_sum = nums[0]
    current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(max_sum, current_sum)

    return max_sum


def func1(nums):
    if not nums:
        return 0
    
    dp = [0] * len(nums)
    dp[0] = nums[0]

    for i in range(1, len(nums)):
        dp[i] = max(dp[i-1] + nums[i], nums[i])

    return max(dp)

    


inp = [1, -2, 3, 10, -4, 7, 2, -5]
print(func(inp))

print(max_sub_array(inp))

print(func1(inp))

