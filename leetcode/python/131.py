class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(s, u):
            if u == len(s): res.append(path.copy())
            else:
                for i in range(u, len(s)):
                    if st[u][i]:
                        path.append(s[u:i+1])
                        dfs(s, i + 1)
                        path.pop()
        res = []
        path = []
        st = [[False] * len(s) for _ in range(len(s))]
        for j in range(len(s)):
            for i in range(0, j+1):
                if i == j: st[i][j] = True
                elif s[i] == s[j]:
                    if i + 1 > j - 1 or st[i+1][j-1]:
                        st[i][j] = True
        dfs(s, 0)
        return res


