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
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def construct_tree(nodes, index=0):
    if index >= len(nodes) or nodes[index] == -1:
        return None
    root = TreeNode(nodes[index])
    root.left = construct_tree(nodes, 2 * index + 1)
    root.right = construct_tree(nodes, 2 * index + 2)
    return root

def max_time_to_spread(root):
    if not root:
        return 0
    left_time = max_time_to_spread(root.left)
    right_time = max_time_to_spread(root.right)
    return root.val + max(left_time, right_time)

def solve(input_list):
    root = construct_tree(input_list)
    # 根节点的值不需要计入传播时间，因为悄悄话是从根节点开始的
    return max_time_to_spread(root) - root.val

# 示例输入
input_list = [0, 9, 20, -1, -1, 15, 7, -1, -1, -1, -1, 3, 2]
print(solve(input_list))  # 输出 38
