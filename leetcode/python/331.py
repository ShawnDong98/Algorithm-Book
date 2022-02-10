class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        def dfs():
            global k, s
            if k == len(s): return False
            if s[k] == '#':
                k += 2
                return True
            while s[k] != ',': k += 1
            k += 1
            return dfs() and dfs()

        k = 0
        s = preorder + ','
        if not dfs(): return False
        return k == len(s)
