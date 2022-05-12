class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def dfs(s, u, k):
            if u == len(s):
                if k == 4:
                    res.append('.'.join(map(str, path)))
                return
            if k == 4: return
            t = 0
            for i in range(u, len(s)):
                if i > u and s[u] == '0': break # 有前导0
                t = t * 10 + int(s[i])
                if t <= 255:
                    path.append(t)
                    dfs(s, i+1, k+1)
                    path.pop()
                else: break
        res = []
        path = []
        dfs(s, 0, 0)
        return res
