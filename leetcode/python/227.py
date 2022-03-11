from collections import defaultdict
class Solution:
    def calculate(self, s: str) -> int:
        def eval():
            b = num.pop()
            a = num.pop()
            c = op.pop()
            if c == '+':  r = a + b
            elif c == '-': r = a - b
            elif c == '*': r = a * b
            else: r = a // b

            num.append(r)

        num = []
        op = []
        pr = defaultdict(int)
        pr['+'] = pr['-'] = 1
        pr['*'] = pr['/'] = 2
        i = 0
        while i < len(s):
            c = s[i]
            if c == ' ':
                i += 1
                continue
            if '0'<=c<='9':
                x, j = 0, i
                # 将连续的数字字符串转换为数字
                while j < len(s) and '0'<=s[j]<='9':
                    x = x*10 + int(s[j])
                    j += 1
                num.append(x)
                i = j - 1
            else:
                while len(op) and pr[op[-1]] >= pr[c]: eval()
                op.append(c)
            i += 1
        while(len(op)): eval()
        return num[-1]

s = " 3/2 "
print(Solution().calculate(s))
