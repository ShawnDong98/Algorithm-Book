from typing import List

class Solution:
    """
        环状排列意味着第一个房子和最后一个房子中只能选择一个偷窃，因此可以把此环状排列房间问题约化为两个单排排列房间子问题：

        - 在不偷窃第一个房子的情况下（即 nums[1:]），最大金额是 p1 
        - 在不偷窃最后一个房子的情况下（即 nums[:n-1]），最大金额是 p2
        - 综合偷窃最大金额： 为以上两种情况的较大值，即 max(p1,p2)。

        状态: 
        - dp[i] 为当前获取的最大金额

        初始状态:
        - dp[0] = nums[0] dp[1] = nums[1]

        状态转移:
        - max(dp[i-2], dp[i-3]) + nums[i]，（注意i == 2的情况额外考虑）
    """
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])

        
        nums1 = nums[1:]
        nums2 = nums[:-1]

        dp1 = [0] * (n-1)
        dp1[0] = nums1[0]
        dp1[1] = nums1[1]

        for i in range(2, (n-1)):
            dp1[i] = max(dp1[i-2], dp1[i-3] if i>=3 else 0) + nums1[i]

        p1 = max(dp1[-1], dp1[-2])

        dp2 = [0] * (n-1)
        dp2[0] = nums2[0]
        dp2[1] = nums2[1]

        for i in range(2, (n-1)):
            dp2[i] = max(dp2[i-2], dp2[i-3] if i>=3 else 0) + nums2[i]

        p2 = max(dp2[-1], dp2[-2])

        return max(p1, p2)
        