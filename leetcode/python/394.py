class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(u):
            res, k = "", 0
            while u < n:
                if s[u].isdigit():
                    k = k * 10 + int(s[u])
                elif s[u] == "[":
                    u, t = dfs(u + 1)
                    res += t * k
                    k = 0
                elif s[u] == "]":
                    return u, res
                else:
                    res += s[u]
                u += 1
            return res

        n = len(s)
        return dfs(0)
