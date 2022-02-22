class Solution:
    def countAndSay_v20220222(self, n: int) -> str:
        s = "1"
        t = ""
        for i in range(n-1):
            j = 0
            while j < len(s):
                k = j + 1
                while k < len(s) and s[k] == s[j]: k += 1
                t += str(k - j) + s[j]
                j = k
            s = t
        return s

    @lru_cache(None)
    def countAndSay(self, n: int) -> str:
    """
        将这个看成两个题， 如何将形如"1211"转换成"111221"
    """
        def count(s):

            ans, cnt = [], 0
            for i, c in enumerate(s + "#"):
                if not i or s[i-1] == c:
                    cnt += 1
                if i and c != s[i-1]:
                    ans.append(str(cnt))
                    ans.append(s[i-1])
                    cnt = 1
            return "".join(ans)
        return "1" if n == 1 else count(countAndSay(n-1))

