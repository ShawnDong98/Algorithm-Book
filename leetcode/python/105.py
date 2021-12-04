class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 递归终止条件
        if not preorder or not inorder: return
        # 先序为 "根左右"， 所以根据 preorder 可以确定 root
        root = TreeNode(preorder[0])
        # 中序为 "左根右"， 所以根据 inorder 可以确定 root 的左右子树
        idx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:1+idx], inorder[:idx])
        root.right = self.buildTree(preorder[1+idx:], inorder[idx+1:])
        return root

