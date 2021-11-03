from typing import List

class Solution:
    """
        使用贪心策略，每一次都选择可以到达最远的地方进行跳跃

        过程：以[2, 3, 1, 1, 4]为例。
            - 开始时站在2，位置索引为0。
            - 第一步跳跃能到的有[3, 1]，最远距离的位置索引是2，对应的元素是1。
            - 第二步跳跃时，从第一步能跳到的区间[3, 1]中选择能跳到最远的位置起跳，因此选择从3的位置开始跳，并更新能跳到的最远距离。
            - 重复上述过程。

    """
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        # 记录每一步跳跃可以到的区间的最后一个元素， 用于记录何时 jumps+=1
        end = 0
        # 记录跳跃次数
        jums = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, nums[i] + i)
            if end == i:
                jums += 1
                end = farthest
        return jums