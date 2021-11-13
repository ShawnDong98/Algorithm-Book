from typing import List

class Solution:
    """
        关注最后一个被戳破的气球k

        状态：
        dp[i][j] 表示开区间(i, j)内能拿到的最多金币

        初始状态：
        dp[i][j] = 0

        状态转移：
        dp[i][j] = max(dp[i][k] + val[k-1] * val[k] * val[k+1] + dp[k][j])

        3, 1, 5, 8 -> 1, 3, 1, 5, 8, 1
        1, 3, 1 (0, 0+2) => store[0][2] = 3

    """
    def maxCoins(self, nums: List[int]) -> int:
        # nums 首尾添加1， 方便处理边界情况
        nums = [1] + nums + [1]

        store = [[0] * len(nums) for _ in range(len(nums))]

        def range_best(i, j):
            m = 0
            # k 是(i, j) 区间内最后一个被戳的气球
            for k in range(i+1, j):
                left = store[i][k]
                right = store[k][j]
                a = left + nums[i] * nums[k] * nums[j] + right
                if a > m:
                    m = a
            store[i][j] = m

        # 对每一个区间长度进行循环
        for n in range(2, len(nums)): # 区间长度从3开始，n从2开始
            # 对于每一个区间长度, 循环区间开头的i
            for i in range(0, len(nums)-n):
                range_best(i, i+n)

        return store[0][len(nums)-1]
