class Solution:
    def convertToBase7(self, num: int) -> str:
        if not num: return "0"
        is_neg = num < 0
        num = abs(num)
        res = ''
        while num:
            res += str(num % 7)
            num //= 7

        res = res[::-1]

        if is_neg: res = '-' + res
        return res
