class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited  = set()
        n = len(isConnected)
        def dfs(i):
            for j in range(n):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)

        num_prov = 0
        for i in range(n):
            if i not in visited: num_prov += 1
            dfs(i)

        return num_prov
