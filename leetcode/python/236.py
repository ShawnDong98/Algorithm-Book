class Solution:
    """
        - 如果以root为根节点的树中，p和q都在树中，则root就是最近公共祖先
        - 如果只包含p， 则返回p
        - 如果只包含q， 则返回q
        - 如果都不包含，则返回None
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if(root is None or root == p or root == q):
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is None: return right
        if right is None: return left

        return root


