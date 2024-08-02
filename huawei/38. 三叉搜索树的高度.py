"""
定义构造三叉搜索树规则如下：每个节点都存有一个数, 当插入一个新的数时, 从根节点向下寻找, 直到找到一个合适的空节点插入。

查找的规则是：

1. 如果数小于节点的数减去500, 则将数插入节点的左子树

2. 如果数大于节点的数加上500, 则将数插入节点的右子树

3. 否则, 将数插入节点的中子树

给你一系列数, 请按以上规则, 按顺序将数插入树中, 构建出一棵三叉搜索树, 最后输出树的高度。

输入描述
第一行为一个数N, 表示有N个数, 1<=N<=10000

第二行为N个空格分隔的整数, 每个数的范围为[1,10000]

输出描述

输出树的高度(根节点的高度为1)。

输入
5000 2000 5000 8000 1800

输出
3

说明
最终构造出的树如下, 高度为3.
"""

from typing import Any


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.mid = None

def insert(root, value):
    if not root:
        return TreeNode(value)
    elif root.value - 500 > value:
        root.left = insert(root.left, value)
    elif root.value + 500 < value:
        root.right = insert(root.right, value)
    else:
        root.mid = insert(root.mid, value)
    return root
    
def get_height(node):
    if not node:
        return 0
    left_height = get_height(node.left)
    right_height = get_height(node.right)
    mid_height = get_height(node.mid)

    return 1 + max(left_height, right_height, mid_height)

def construct_tree_and_get_height(values):
    if not values:
        return 0
    
    root = TreeNode(values[0])

    for value in values[1:]:
        insert(root, value)

    return get_height(root)



 

N = int(input())

inp = list(map(int, input().split()))

print(construct_tree_and_get_height(inp))

