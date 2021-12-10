class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(s):
            if len(s) % 2 == 0:
                a = s[:len(s)//2]
                b = s[len(s)//2:]
            else:
                a = s[:(len(s)-1)//2]
                b = s[(len(s)-1)//2+1:]
            if a != b[::-1]:
                return False
            return True

        if len(s) <= 1:
            return '' if len(s) == 0 else s[0]
        else:
            dp = [1] * len(s)
            for i in range(1, len(s)):
                for j in range(i-1-dp[i-1], i):
                    if j < 0:
                        continue
                    if isPalindrome(s[j:i+1]):
                        dp[i] = i + 1 - j
                        break

        maxl = max(dp)
        maxindex = dp.index(max(dp))
        return s[maxindex-maxl+1:maxindex+1]


