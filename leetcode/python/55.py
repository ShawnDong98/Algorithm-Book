from typing import List

class Solution:
    """
        如果能到达某个位置，那一定能到达它前面的所有位置。
    """
    def canJump(self, nums: List[int]) -> bool:
        # 初始化当前能到达的最远的位置
        max_i = 0
        # i 为当前位置， jump是当前位置的跳数
        for i, jump in enumerate(nums):
            # 如果当前位置能到达最远的位置，并且当前位置+跳数>最远位置
            if max_i >= i and i + jump > max_i:
                max_i = i + jump

        return max_i >= i

    def canJump_solution2(self, nums: List[int]) -> bool:
        # 初始化当前能到达的最远的位置
        farthest = 0
        # i 为当前位置， jump是当前位置的跳数
        for i, jump in enumerate(nums):
            # 如果当前位置小于最远的位置，并且当前位置+跳数>最远位置
            if i  <= farthest:
                farthest = max(farthest, i + jump)

        return farthest >= i
             