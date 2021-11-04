# from typing import List

# class Solution:
#     def wiggleMaxLength(self, nums: List[int]) -> int:
#         # c 是用来记录前一个差值是下降还是上升的， 默认0
#         n, c, res = len(nums), 0, 1
#         if n < 2:
#             return n
#         for i in range(1, n):
#             x = nums[i] - nums[i - 1]
#             # 如果有差值才继续处理，相等直接跳过不处理
#             if x:
#                 # <0 代表有上升下降的交替， =0是初始情况的判断
#                 if x * c <= 0:
#                     res += 1
#                 c = x
#         return res 

from typing import List
from itertools import groupby

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        nums = [k for k, g in groupby(nums)]
        if len(nums) <= 2:
            return len(nums)
        
        res = 2
        for i in range(1, len(nums)-1):
            a = nums[i - 1]
            b = nums[i]
            c = nums[i + 1]
            if (a < b and b > c):
                res += 1
            elif (a > b and b < c):
                res += 1

        return res

