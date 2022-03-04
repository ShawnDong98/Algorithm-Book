class Solution:
    def __init__(self):
        self.nt = ["Zero", "One", "Two", "Three", "Four", "Five","Six", "Seven", "Eight", "Nine", \
                   "Ten","Eleven","Twelve","Thirteen","Fourteen", "Fifteen","Sixteen","Seventeen", \
                   "Eighteen", "Nineteen"]
        self.tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty",\
 "Ninety"]
        self.t = ["Thousand", "Million", "Billion", ""]
    def numberToWords_v20220304(self, num: int) -> str:
        def get(x):
            res = ''
            if x >= 100:
                res += self.nt[x // 100] + " Hundred "
                x %= 100
            if x >= 20:
                res += self.tens[x // 10] + ' '
                x %= 10
                if x: res += self.nt[x] + ' '
            elif x:
                res += self.nt[x] + ' '
            return res
        if not num: return 'Zero'
        res = ''
        i, j = 1000000000, 0
        while i >= 1:
            if num >= i:
                res += get(num // i) + self.t[j] + ' '
                num %= i
            i //= 1000
            j += 1
        return res.strip()
    def numberToWords(self, num: int) -> str:
        def helper(num) -> List[str]:
            if num < 20:
                return [self.nt[num]]
            elif num < 100:
                res = [self.tens[num//10]]
                if num % 10:
                    res += helper(num % 10)
                return res
            elif num < 1000:
                res = [self.nt[num//100], "Hundred"]
                if num % 100:
                    res += helper(num%100)
                return res
            for p, w in enumerate(self.t, 1):
                if num < 1000 ** (p + 1):
                    return helper(num // 1000 ** p) + [w] + helper(num % 1000 ** p) \
                        if num % 1000 ** p else helper(num // 1000 ** p) + [w]
        return " ".join(helper(num))

