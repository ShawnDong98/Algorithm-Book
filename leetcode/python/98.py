class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.dfs(root, -(2**32), 2**32)

    def dfs(self, root, minv, maxv):
        if not root: return True
        if root.val < minv or root.val > maxv: return False
        return self.dfs(root.left, minv, root.val-1) and self.dfs(root.right, root.val+1, maxv)
