"""
题目：请实现一个函数用来匹配包含'.'和'*'的正则表达式。模式中的字符 '.' 表示任意一个字符，而 “*”* 表示它前面的字符可以出现任意次（含 0 次）。

在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。
"""

def is_match(s, p):
    len_s = len(s)
    len_p = len(p)
    dp = [[False] * (len_p+1)  for _ in range(len_s+1)]
    dp[0][0] = True

    for j in range(2, len_p+1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-2]

    for i in range(1, len_s+1):
        for j in range(1, len_p+1):
            if p[j-1] == "." or p[j-1] == s[i-1]:
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == "*":
                dp[i][j] = dp[i][j-2] or (dp[i-1][j] and (p[j-2] == s[i-1] or p[j-2]=="."))
    
    return dp[len_s][len_p]


print(is_match("aaa", "a.a"))
print(is_match("aaa", "ab*ac*a"))
print(is_match("aaa", "aa.a"))
print(is_match("aaa", "ab*a"))