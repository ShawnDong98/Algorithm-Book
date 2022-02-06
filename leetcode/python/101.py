class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(p, q):
            if not p and not q: return True
            if not p or not q or p.val != q.val: return False
            return dfs(p.left, q.right) and dfs(p.right, q.left)
        if not root: return True
        return dfs(root.left, root.right)
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(left, right):
            if not left and not right: return True
            elif not left or not right: return False
            elif left.val != right.val: return False
            else:
                return dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root.left, root.right)
