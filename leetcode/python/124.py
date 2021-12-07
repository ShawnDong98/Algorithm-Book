from typing import Optional

class Solution:
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
