class Solution:
    """
    与最长递增子序列问题类似:
    状态:
        dp[i]: dp[i] 是以 i 结尾的分割成回文串的最少次数
        
    状态转移方程:
        dp[i] = min(dp[i], dp[j] + 1); 如果 isPalindrome(s[j + 1..i])

    """
    def minCut(self, s: str) -> int:
        N = len(s)
        dp = [N] * N
        for i in range(N):
            if self.isPalindrom(s[0:i+1]):
                dp[i] = 0
                continue
            for j in range(i):
                if self.isPalindrome(s[j+1:i+1]):
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[N-1]
        
    def isPalindrome(self, s):
        return s == s[::-1]