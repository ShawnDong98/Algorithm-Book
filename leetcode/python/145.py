class Solution:
    def postorderTraversal_v20220208(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stk = []
        while root or len(stk):
            while root:
                res.append(root.val)
                stk.append(root)
                root = root.right

            root = stk.pop().left
            stk.pop()
        return res[::-1]
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(root):
            if root is None: return
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)
        dfs(root)
        return res
