"""
给定一个二叉树，每个节点上站着一个人，节点数字表示父节点到该节点传递悄悄话需要花费的时间。初始时，根节点所在位置的人有一个悄悄话想要传递给其他人，求二叉树所有节点上的人都接收到悄悄话花费的时间。

输入描述：

0 9 20 -1 -1 15 7 -1 -1 -1 -1 3 2
注：-1表示空节点

输出描述：
返回所有节点都接收到悄悄话花费的时间38

示例1:
输入：

0 9 20 -1 -1 15 7 -1 -1 -1 -1 3 2
输出：

38
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def BuildTree(nodes, index):
    if index >= len(nodes) or nodes[index] == -1:
        return None
    
    root = TreeNode(nodes[index])

    root.left = BuildTree(nodes, 2 * index + 1)
    root.right = BuildTree(nodes, 2 * index + 2)

    return root


def max_depth(root):
    if not root:
        return 0

    val = root.val

    left = val + max_depth(root.left)
    right = val + max_depth(root.right)

    return max(left, right)


nodes = list(map(int, input().split()))

root = BuildTree(nodes, 0)

print(max_depth(root))
