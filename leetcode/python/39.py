class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(c, u, target):
            if target == 0:
                res.append(path.copy())
                return
            if u == len(c): return

            i = 0
            while c[u] * i <= target:
                dfs(c, u + 1, target - c[u] * i)
                path.append(c[u])
                i += 1

            i = 0
            while c[u] * i <= target:
                path.pop()
                i += 1

        res = []
        path = []
        dfs(candidates, 0, target)
        return res
