class Solution:
    """
        如果选择 i 为根节点，那么左子树共有 i - 1 个节点，右子树共有 n - i 个节点

        dp[i] 含义：i 个节点组成的二叉搜索树数量

        当只有0个节点时，此时只有空树这一种二叉树，dp[0] = 1

        需要通过状态转移求得 dp[n]，分别选择1, 2, …, n为根节点，每种根节点对应的二叉树数量为其左子树数量乘以右子树数量

        dp[n]=dp[0]∗dp[n−1]+dp[1]∗dp[n−2]+…+dp[n−1]∗dp[0]

        因此需要两层循环计算 dp[n]，外层循环遍历节点个数从1到n的所有情况，内层循环计算每种根节点对应的二叉树数量并求和。转移方程如下：

                    dp[i]+=dp[j]∗dp[i−j−1]
        
        最后返回dp[-1]，即dp[n]
    """
    def numTrees(self, n: int) -> int:
        dp = [1] + [0] * n
        for i in range(1, n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[-1]
