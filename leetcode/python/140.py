from typing import List

class Solution:
    """
        状态：
            dp[i] 表示 s[:i] 是否可以分割
            pos[i]=[j1, j2..jk]表示前i个字符可以由前j1，j2..jk以及他们之后的字符拆分。
        
        状态转移方程：
            dp[i] = (dp[0] & s[0:i+1] in word) |......|(dp[i - 1] and s[i])
            并且将其中为True的那一项对应的j添加到pos[i]中
        
        dfs根据pos拆分原始字符串
            pos[i]记录了所有满足条件的j，即前j个字符组成的字符串可拆分且j到i的字符串在word中，因此我们可以通过深度遍历的思想访问所有情形。
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        length = 0
        for t in wordDict:
            length = max(length, len(t))
        wordDict = set(wordDict)
        # 记录前 i 个字符是否可以拆分
        dp = [False] * (n + 1)
        # 记录前 i 个字符的状态来源
        pos = [[] for _ in range(n + 1)]
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i, i - length, -1):
                if j > 0 and s[j-1:i] in wordDict:
                    if dp[j-1]:
                        dp[i] = True
                        pos[i].append(j-1)

        if not dp[n]:
            return []

        res = [] 

        def dfs(start, path:str):
            if start == 0: 
                res.append(path[:-1])
            else:
                for t in pos[start]:
                    dfs(t, s[t:start] + ' ' + path)

        dfs(n, '')
        return res