from functools import lru_cache
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        @lru_cache(None)
        def dfs(x, s):
            for i in range(n):
                if (x >> i) & 1:
                    continue
                if s + i + 1 >= m:
                    return True
                if not dfs(x + (1 << i), s + i + 1):
                    return True

            return False

        n = maxChoosableInteger
        m = desiredTotal
        if n * (n + 1) / 2 < m:
            return False
        return dfs(0, 0)
