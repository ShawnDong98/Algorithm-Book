class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(n, k, start):
            if k == 0:
                res.append(path.copy())
                return
            for i in range(start, n+1):
                path.append(i)
                dfs(n, k-1, i+1)
                path.pop()

        res = []
        path = []
        dfs(n, k, 1)
        return res

