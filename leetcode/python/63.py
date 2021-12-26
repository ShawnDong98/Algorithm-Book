from typing import List

class Solution:
    """
    状态：
    - dp[i][j]: 走到当前格子有多少中不同的走法

    状态转移:
    - dp[i][j] = dp[i-1][j] + dp[i][j-1], 遇到障碍物跳过
    """
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]

        for i in range(n):
            if obstacleGrid[0][i] == 1:
                break
            dp[0][i] = 1

        for j in range(m):
            if obstacleGrid[j][0] == 1:
                break
            dp[j][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]
