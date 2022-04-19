from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow_v20220419(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        for i in range(len(nums)):
            if q and i - k + 1 > q[0]: q.popleft()
            while q and nums[i] >= nums[q[-1]]: q.pop()
            q.append(i)
            if i >= k - 1: res.append(nums[q[0]])
        return res
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q, ret = deque(), []
        for i, j in enumerate(nums):
            while q and nums[q[-1]] < j:
                q.pop()
            if q and q[0] <= i - k:
                q.popleft()
            q.append(i)
            if i >= k - 1:
                ret.append(nums[q[0]])
        return ret

    def maxSlidingWindow_tle(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= k: return [max(nums)]
        left = 0
        right = left + k
        res = []
        while right <= len(nums):
            res.append(max(nums[left:right]))
            left += 1
            right += 1
        return res
