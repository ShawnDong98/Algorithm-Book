"""
给一个正整数列 nums, 一个跳数 jump, 及幸存数量 left。运算过程为: 从索引为 0 的位置开始向后跳, 中间跳过 jump 个数字, 命中索引为 jump + 1 的数字, 该数被敲出, 并从该点起跳, 以此类推, 直到幸存 left 个数为止。然后返回幸存数之和。

约束: 

1. 0 是第一个起跳点。
2. 起跳点和命中点之间间隔 jump 个数字, 已被敲出的数字不计入在内。
3. 跳到末尾时无缝从头开始（循环查找）, 并可以多次循环。
4. 若起始时 left > len(nums) 则无需跳数处理过程。

示例1
输入: [1,2,3,4,5,6,7,8,9],4,3
输出:13
说明:从1(索引为0)开始起跳,中间跳过4个数字,因此依次删除 6,2,8,5,4,7 。 剩余 1,3,9, 返回和为13
"""

def find_lucky(nums, left, jump):
    if left > len(nums):
        return sum(nums) 
    
    idx = 0
    while left < len(nums):
        idx += jump + 1 
        idx %= len(nums)
        nums.pop(idx)
        idx -= 1

    return sum(nums)


inp = input()

left = int(inp[-1])
jump = int(inp[-3])

nums = list(map(int, inp[1:-5].split(',')))

print(find_lucky(nums, left, jump))




     




























