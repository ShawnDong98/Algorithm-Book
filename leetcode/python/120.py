from typing import List
import copy

class Solution:
    """
    状态：
    - dp[i][j]: 到达当前节点的最小路径和


    状态转移：
    - 上一层节点的最小路径加上当前节点
        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    
    """
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return min(triangle[0])
        # 处理边界
        for i in range(len(triangle)):
            triangle[i] = [float('inf')] + triangle[i] + [float('inf')]
        dp = copy.deepcopy(triangle)
        for i in range(1, len(triangle)):
            for j in range(1, len(triangle[i])-1):
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        return min(dp[-1])

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
s = Solution()
print(s.minimumTotal(triangle))