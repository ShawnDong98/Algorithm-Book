class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        def dfs(bottom, up, u):
            if len(bottom) == 1: return True
            if u == len(bottom) - 1: return dfs(up, "", 0)

            for c in g[ord(bottom[u])-ord('A')][ord(bottom[u+1]) - ord('A')]:
                if dfs(bottom, up + c, u + 1):
                    return True

            return False

        g = [[[] for _ in range(7)] for _ in range(7)]
        for s in allowed: g[ord(s[0]) - ord('A')][ord(s[1]) - ord('A')].append(s[2])
        return dfs(bottom, "", 0)
