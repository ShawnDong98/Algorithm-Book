"""
题目：给出一个二叉树如下图所示：

```
          6
         / \\
        7   9
         \\  /
         -2 6

```

请由该二叉树生成一个新的二叉树, 它满足其树中的每个节点将包含原始树中的左子树和右子树的和。

```
          20 (7-2+9+6)
         /   \\
        -2    6
         \\   /
          0 0

```

左子树表示该节点左侧叶子节点为根节点的一颗新树；右子树表示该节点右侧叶子节点为根节点的一颗新树。

输入描述
2行整数, 第1行表示二叉树的中序遍历, 第2行表示二叉树的前序遍历, 以空格分割

例如：

7 -2 6 6 9

6 7 -2 9 6

输出描述
1行整数, 表示求和树的中序遍历, 以空格分割

例如：

输出

-2 0 20 0 6

示例1
输入：
-3 12 6 8 9 -10 -7
8 12 -3 6 -10 9 -7

输出：
0 3 0 7 0 2 0
"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# def BuildTree(PreOrder, MidOrder):
#     if not PreOrder or not MidOrder:
#         return None
    
#     half = len(PreOrder) // 2
#     root = TreeNode(PreOrder[0])
#     PreOrder_Left = PreOrder[1:1+half]
#     PreOrder_Right = PreOrder[1+half:]

#     MidOrder_Left = MidOrder[:half]
#     MidOrder_Right = MidOrder[half+2:]

#     root.left = BuildTree(PreOrder_Left, MidOrder_Left)
#     root.right = BuildTree(PreOrder_Right, MidOrder_Right)

#     return root


def BuildTree(preorder, inorder):
    if not preorder or not inorder:
        return None
    
    root = TreeNode(preorder[0])
    print(inorder)
    root_index_inorder = inorder.index(root.val)

    inorder_left = inorder[:root_index_inorder]
    inorder_right = inorder[root_index_inorder+1:]

    preorder_left = preorder[1:1+len(inorder_left)]
    preorder_right = preorder[1+len(inorder_left):]

    root.left = BuildTree(preorder_left, inorder_left)
    root.right = BuildTree(preorder_right, inorder_right)

    return root



def sum_tree(root):
    if not root:
        return 0
    
    root.val = root.left.val + root.right.val
    sum_tree(root.left)
    sum_tree(root.right)

    return root

# def print_mid_order(root):
#     if not root:
#         return None
#     print_mid_order(root.left)
#     print(root.val)
#     print_mid_order(root.right)

# 辅助函数打印树（中序遍历）
def print_mid_order(node):
    if node:
        print_mid_order(node.left)
        print(node.val, end=' ')
        print_mid_order(node.right)

PreOrder = list(map(int, input().split()))
MidOrder = list(map(int, input().split()))

root = BuildTree(PreOrder, MidOrder)
print(root)
print_mid_order(root)