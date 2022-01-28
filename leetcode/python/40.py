class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, u, target):
            if target == 0:
                res.append(path.copy())
                return
            if u == len(c): return

            k = u + 1
            while k < len(c) and c[k] == c[u]: k += 1
            cnt = k - u

            i = 0
            while c[u] * i <= target and i <= cnt:
                dfs(c, k, target - c[u] * i)
                path.append(c[u])
                i += 1

            i = 0
            while c[u] * i <= target and i <= cnt:
                path.pop()
                i += 1

        res = []
        path = []
        c = sorted(candidates)
        dfs(c, 0, target)
        return res
