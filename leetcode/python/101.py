class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(left, right):
            if not left and not right: return True
            elif not left or not right: return False
            elif left.val != right.val: return False
            else:
                return dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root.left, root.right)
