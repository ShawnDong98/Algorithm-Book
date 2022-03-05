class Solution:
    def convert_v20220305(self, s: str, numRows: int) -> str:
        res = ''
        if numRows == 1: return s
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                j = i
                while j < len(s):
                    res += s[j]
                    j += 2 * numRows - 2
            else:
                j = i
                k = 2 * numRows - 2 - i
                while j < len(s) or k < len(s):
                    if j < len(s): res += s[j]
                    if k < len(s): res += s[k]
                    j += 2 * numRows - 2
                    k += 2 * numRows - 2
        return res
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = [''] * numRows
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i==numRows - 1: flag = -flag
            i += flag

        return ''.join(res)
