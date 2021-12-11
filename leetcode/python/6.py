clas Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = [''] * numRows
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i==numRows - 1: flag = -flag
            i += flag

        return ''.join(res)
