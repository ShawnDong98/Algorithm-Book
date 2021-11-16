from typing import List

class Solution:
    """
    由于宽和高都是按照从小到大的顺序排列，在遍历高h时，可能两者宽w相等，后面信封高大于前者需要另外判断，比较繁琐，所以可以将高h按照从大到小的顺序排列，便无需再判断两者的宽w是否相等，从而转化为了一维的最长上升子序列问题

    状态： 
    - dp[i] 表示以 i 结尾的最长递增子序列的长度

    状态转移：
    - dp[i] = max(dp[i], dp[j] + 1)
    
    """
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes: 
            return 0

        N = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = [1] * N
        for i in range(1, N):
            for j in range(i):
                if envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)