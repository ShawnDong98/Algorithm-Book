from typing import List

class Solution:
    """
    dp[i][j]表示以第i行，第j列处为右下角的最大正方形的边长
    仅当该位置为11时，才有可能存在正方形。且递推公式为：
        dp[i][j]=min(dp[i−1][j−1],dp[i−1][j],dp[i][j−1])+1。
    含义为若当前位置为1，则此处可以构成的最大正方形的边长，是其正上方，左侧，和左上界三者共同约束的，且为三者中的最小值加1。
    - 特判，若matrix为空，返回0
    - 初始化matrix的行m，列n，初始化dp=[[0,...,0],...,[0,...,0]]，维度为(m+1)*(n+1)，这样便于处理。初试化最大边长res=0。
    - 遍历dp数组，遍历行i，遍历区间[1,m+1)：
    - - 遍历列j，遍历区间[1,n+1)：
    - - - 若matrix[i-1][j-1]=="1，此时可能存在正方形：
            dp[i][j]=min(dp[i−1][j−1],dp[i−1][j],dp[i][j−1])+1
    - - - 并更新最大边长res=max(res,dp[i][j])
    - 返回面积res*res
    """
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if (not matrix):
            return 0
        m = len(matrix)
        n = len(matrix[0])
        res = 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if (matrix[i - 1][j - 1] == '1'):
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                    res = max(res, dp[i][j])
        return res * res