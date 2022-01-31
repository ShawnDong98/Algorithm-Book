class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(n, lc, rc, seq):
            if lc == n and rc == n:
                res.append(seq)
            else:
                if lc < n: dfs(n, lc + 1, rc, seq +'(')
                if rc < n and lc > rc: dfs(n, lc, rc + 1, seq + ')')

        res = []
        dfs(n, 0, 0, "")
        return res
