class Solution:
    """
    状态：
    dp[i][j][k]表示球k次操作后移到i,j位置的路径数

    状态转移：
    遍历K次矩阵m*n 且 dp[i][j][k]>0有值的情况下，尝试相邻四个方向作为k+1次操作：
    - 若k+1次未出界，则把第k次dp[i][j][k]累加到dp[i][j][k+1]
    - 若k+1次出界，则把第k次dp[i][j][k]累加到最终结果

    界情况：dp[startRow][startColumn][0]=1
    """
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        ans, mod = 0, 10**9 + 7
        dp = [[[0]*(maxMove+1) for _ in range(n)] for _ in range(m)]
        dp[startRow][startColumn][0] = 1

        for k in range(maxMove):
            for i in range(m): 
                for j in range(n): 
                    if dp[i][j][k] > 0:
                        for ii, jj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                            if 0 <= ii < m and 0 <= jj < n:
                                dp[ii][jj][k+1] = (dp[ii][jj][k+1] + dp[i][j][k]) % mod
                            else:
                                ans = (ans + dp[i][j][k]) % mod
        return ans