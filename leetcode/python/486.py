from typing import List

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        length = len(nums)

        if length == 1:
            return True
        
        dp = [[0] * length for i in range(length)]

        for i in range(length):
            dp[i][i] = nums[i]

        for m in range(1, length):
            for n in range(length - m):
                dp[n][n+m] = max(nums[n] - dp[n+1][n+m], nums[n+m] - dp[n][n+m-1]) 

        return dp[0][length-1] >= 0