class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        if len(strs)==0: return res

        for i in range(201):
            if i >= len(strs[0]): return res
            c = strs[0][i]
            for str_ in strs:
                if len(str_) <= i or str_[i] != c:
                    return res
            res += c

        return res
