class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def dfs(s, u):
            if u == len(s): res.append("".join(s))
            else:
                dfs(s, u + 1)
                if s[u].isalpha():
                    s[u] = s[u].swapcase()
                    dfs(s, u+1)
                    s[u] = s[u].swapcase()

        res = []
        dfs(list(s), 0)
        return res
