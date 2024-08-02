"""
机器人搬砖, 一共有N堆砖存放在N个不同的仓库中, 第i堆砖中有bricks[i]块砖头, 要求在8小时内搬完。机器人每小时能搬砖的数量取决于有多少能量格, 机器人一个小时中只能在一个仓库中搬砖, 机器人的能量格每小时补充一次且能量格只在这一个小时有效, 为使得机器人损耗最小化尽量减小每次补充的能量格数。为了保障在8小时内能完成搬砖任务, 请计算每小时给机器人充能的最小能量格数。

备注：
1、不需考虑机器人补充能量格的耗时; 
2、不需考虑机器人搬砖的耗时; 
3、机器人每小时补充能量格只在这一个小时中有效。

输入描述
程序有输入为“30 12 25 8 19”一个整数数组, 数组中的每个数字代表第i堆砖的个数, 每堆砖的个数不超过100

输出描述
输出在8小时内完成搬砖任务, 机器人每小时最少需要充多少个能量格; 

如果8个小时内无法完成任务, 则输出“-1”; 

示例1
输入：
30 12 25 8 19

输出：
15

示例2
输入：
10 12 25 8 19 8 6 4 17 19 20 30

输出：
-1

说明：
砖的堆数为12堆存放在12个仓库中, 机器人一个小时内只能在一个仓库搬砖, 不可能完成任务
"""
import math

def func(bricks):
    if len(bricks) > 8:
        return -1
    
    def can_finish_with_energy(K):
        hours_needed = 0
        for b in bricks:
            hours_needed += math.ceil(b / K)

        return hours_needed <= 8
    
    left, right = 1, max(bricks)

    while left <= right:
        mid = (left + right) // 2
        if can_finish_with_energy(mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result





bricks = list(map(int, input().split()))

print(func(bricks))
