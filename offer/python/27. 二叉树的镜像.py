"""
请完成一个函数 输入一棵二叉树 该函数输出它的镜像
"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def flip(tree):
    if not tree:
        return None
    temp = flip(tree.left)
    tree.left = flip(tree.right)
    tree.right = temp

    return tree


# 辅助函数：前序遍历打印树的节点值
def preOrderTraversal(root):
    if root:
        print(root.val, end=' ')
        preOrderTraversal(root.left)
        preOrderTraversal(root.right)

# 构建示例二叉树
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("原二叉树的前序遍历：")
preOrderTraversal(root)
print()

# 镜像二叉树
flip(root)

print("镜像二叉树的前序遍历：")
preOrderTraversal(root)