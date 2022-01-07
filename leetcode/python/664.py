class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        
        for Len in range(2, n + 1):
            for L in range(0, n - Len + 1):
                R = L + Len - 1
                dp[L][R] = dp[L][R-1] + 1
                for mid in range(L, R):
                    if s[mid] == s[R]:
                        dp[L][R] = min(dp[L][R], dp[L][mid] + dp[mid+1][R-1])
                        dp[L][R] = min(dp[L][R], dp[L][mid] + dp[mid+1][R-1])


        return dp[0][n-1]