
class Solution:
    """
    状态：
    dp[i]: 若前 i 个字符可以解码， 表示前 i 个字符可以解码的方法数

    若前 i 个字符不能解码，那整个字符串肯定不能解码，我们无需再进行下去了，直接返回 0 即可

    """
    def numDecodings(self, s: str) -> int:
        # 开头有 0 直接返回
        if s.startswith('0'):
            return 0

        n = len(s)
        dp = [1] * (n+1)

        for i in range(2, n+1):
            if s[i-1] == '0' and s[i-2] not in '12':
                return 0
            # 只有组合在一起才能解码
            if s[i-2:i] in ['10', '20']:
                dp[i] = dp[i-2]
            # 有两种解码方式
            elif '10' < s[i-2:i] <= '26':
                dp[i] = dp[i-1] + dp[i-2]
            else:
                # '01' 到 '09' 或 > '26'，只有单独才能解码 
                dp[i] = dp[i-1]
        return dp[n]


s = "1201234"
S= Solution()
print(S.numDecodings(s))