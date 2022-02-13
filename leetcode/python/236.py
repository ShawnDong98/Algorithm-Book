class Solution:
    def lowestCommonAncestor_v20220213(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root, p, q):
            nonlocal res
            if not root: return 0
            state = dfs(root.left, p, q)
            if root == p: state |= 1
            elif root == q: state |= 2
            state |= dfs(root.right, p, q)
            if state == 3 and not res: res = root
            return state
        res = None
        dfs(root, p, q)
        return res
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
            - 如果以root为根节点的树中，p和q都在树中，则root就是最近公共祖先
            - 如果只包含p， 则返回p
            - 如果只包含q， 则返回q
            - 如果都不包含，则返回None
        """
        if(root is None or root == p or root == q):
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is None: return right
        if right is None: return left

        return root


