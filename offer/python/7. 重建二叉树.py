"""
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如，输入前序遍历序列(1,2,4,7,3.5,6.8}和中序遍历序列{4,7,2,1,5,3,8,6}
"""

class TreeNode:
    def __init__(self, v):
        self.left = None
        self.right = None
        self.val = v


def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None
    
    root = TreeNode(preorder[0])
    root_index_inorder = inorder.index(root.val)

    inorder_left = inorder[:root_index_inorder]
    inorder_right = inorder[root_index_inorder+1:]

    preorder_left = preorder[1:1+len(inorder_left)]
    preorder_right = preorder[1+len(inorder_left):]

    root.left = build_tree(preorder_left, inorder_left)
    root.right = build_tree(preorder_right, inorder_right)

    return root

# 测试用例
preorder = [1, 2, 4, 7, 3, 5, 6, 8]
inorder = [4, 7, 2, 1, 5, 3, 8, 6]

root = build_tree(preorder, inorder)

# 辅助函数打印树（中序遍历）
def printTreeInOrder(node):
    if node:
        printTreeInOrder(node.left)
        print(node.val, end=' ')
        printTreeInOrder(node.right)

print("重建的二叉树的中序遍历结果：")
printTreeInOrder(root)


