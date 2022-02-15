class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(root):
            nonlocal res
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)
            return max(left, right) + 1
        res = 0
        dfs(root)
        return res
