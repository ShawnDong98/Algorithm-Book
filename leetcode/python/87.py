class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        f = [[[False] * (n+1) for _ in range(n)] for _ in range(n)]
        for k in range(1, n+1):
            i = 0
            while i + k - 1 < n:
                j = 0
                while j + k - 1 < n:
                    if k == 1:
                        if s1[i] == s2[j]: f[i][j][k] = True
                    else:
                        for u in range(1, k):
                            if f[i][j][u] and f[i+u][j+u][k-u] or f[i][j+k-u][u] and f[i+u][j][k-u]:
                                f[i][j][k] = True
                                break
                        else:
                            f[i][j][k] = False
                    j += 1
                i += 1
        return f[0][0][n]
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True
        bs1, bs2 = sorted(s1), sorted(s2)
        if bs1 != bs2: return False

        n = len(s1)
        for i in range(1, n):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True

        return False
