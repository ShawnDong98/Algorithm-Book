from collections import defaultdict
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        x, y = numerator, denominator
        if x % y == 0: return str(x // y)
        res = ''
        if (x < 0) ^ (y < 0): res += '-'
        x = abs(x)
        y = abs(y)
        res += str(x // y) + '.'
        x %= y
        hash = defaultdict(int)
        while x:
            hash[x] = len(res)
            x *= 10
            res += str(x // y)
            x %= y
            if hash[x] != 0:
                res = res[:hash[x]] + '(' + res[hash[x]:] + ')'
                break
        return res

