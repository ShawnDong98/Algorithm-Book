class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(root):
            path.append(root.val)
            if not root.left and not root.right:
                res.append('->'.join(map(str, path)))
            else:
                if root.left: dfs(root.left)
                if root.right: dfs(root.right)
            path.pop()

        res = []
        path = []
        if root: dfs(root)
        return res
