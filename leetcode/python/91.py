class Solution:
    def numDecodings_20211226(self, s: str) -> int:
        """
        状态表示：
        - 集合： 所有前 i 个数字解码得到的字符串
        - 属性： 数量

        状态计算：
        - 最后一个字母是一位数 f[i-1]
        - 最后一个字母是两位数 f[i-2]
        """
        if not s: return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(1, len(s) + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            if i!=1 and s[i-2:i] > '09' and s[i-2:i] < '27':
                dp[i] += dp[i - 2]
        return dp[len(s)]

    def numDecodings(self, s: str) -> int:
        """
        状态：
        dp[i]: 若前 i 个字符可以解码， 表示前 i 个字符可以解码的方法数

        若前 i 个字符不能解码，那整个字符串肯定不能解码，我们无需再进行下去了，直接返回 0 即可

        """
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
