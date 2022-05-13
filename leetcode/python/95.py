class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def dfs(l, r):
            if l > r: return [None,]
            res = []

            for i in range(l, r + 1):
                left = dfs(l , i - 1)
                right = dfs(i + 1, r)
                for j in left:
                    for k in right:
                        root = TreeNode(i)
                        root.left = j
                        root.right = k
                        res.append(root)
            return res
        if not n: return []
        return dfs(1, n)
