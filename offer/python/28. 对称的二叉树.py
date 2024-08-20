"""
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。
"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_mirror_tree(tree):
    if not tree:
        return True
    
    return is_mirror(tree.left, tree.right)
    

def is_mirror(left, right):
    if not left and not right:
        return True 
    
    if not left and right:
        return False
    
    if left and not right:
        return False

    return left.val == right.val and is_mirror(left.left, right.right) and is_mirror(left.right, right.left)


# 构建示例二叉树
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(4)

print(is_mirror_tree(root))