from typing import Optional

class Solution:
    def maxPathSum_v20220216(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            nonlocal res
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right + root.val)
            return max(0, max(left, right) + root.val)
        res = float('-inf')
        dfs(root)
        return res
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxsum = float('-inf')
        def dfs(root):
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.maxsum = max(self.maxsum, left + right + root.val)
            return max(0, max(left, right) + root.val)
        print(dfs(root))
        return self.maxsum
