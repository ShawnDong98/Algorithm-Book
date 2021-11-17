from typing import List

class Solution:
    """
    初始化：
    - 定义与 matrix 大小相同的 dp 列表，并用 1 填充；
    - 定义 numsSort 列表保存排序后的 matrix。（保存值和索引）

    填充：
    - 用i、j、k循环numsSort列表：
    - - 填充为以下几种的最大值+1
    - - - 如果j不是0且matrix[j-1][k]<i则是dp[j-1][k]，其他情况是0；
    - - - 如果k不是0且matrix[j][k-1]<i则是dp[j][k-1]，其他情况是0；
    - - - 如果j不是len(matrix)-1且matrix[j+1][k]<i则是dp[j+1][k]，其他情况是0
    - - - 如果k不是len(matrix[0])-1且matrix[j][k+1]<i则是dp[j][k+1]，其他情况是0。

    返回：返回sum(dp, [])的最大值
    """
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        x = len(matrix)
        y = len(matrix[0])
        dp = [[1 for __ in range(y)] for __ in range(x)]
        numsSort = sorted(sum([[(matrix[i][j], i, j) for j in range(y)] 
        for i in range(x)], []))

        for i, j, k in numsSort:
            dp[j][k] = 1 + max(
                dp[j-1][k] if j and matrix[j-1][k]<i else 0,
                dp[j][k-1] if k and matrix[j][k-1]<i else 0,
                dp[j+1][k] if j != x-1 and matrix[j+1][k]<i else 0,
                dp[j][k+1] if k != y-1 and matrix[j][k+1]<i else 0
            )

        return max(sum(dp, []))




matrix = [[9,9,4],[6,6,8],[2,1,1]]
S = Solution()
print(S.longestIncreasingPath(matrix))