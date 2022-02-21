class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(root):
            if not root: return [0, 0]
            x = dfs(root.left)
            y = dfs(root.right)
            return [max(x[0], x[1]) + max(y[0], y[1]), x[0] + y[0] + root.val]
        f = dfs(root)
        return max(f[0], f[1])
