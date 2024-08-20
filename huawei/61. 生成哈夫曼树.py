"""
给定长度为n的无序的数字数组, 每个数字代表二叉树的叶子节点的权值, 数字数组的值均大于等于1。请完成一个函数, 根据输入的数字数组, 生成哈夫曼树, 并将哈夫曼树按照中序遍历输出。为了保证输出的二叉树中序遍历结果统一, 增加以下限制：二叉树节点中, 左节点权值小于等于右节点权值, 根节点权值为左右节点权值之和。当左右节点权值相同时, 左子树高度小于等于右子树。注意：所有用例保证有效, 并能生成哈夫曼树。提醒：哈夫曼树又称最优二叉树, 是一种带权路径长度最短的二叉树。所谓树的带权路径长度, 就是树中所有的叶结点的权值乘上其到根结点的路径长度(若根结点为0层, 叶结点到根结点的路径长度为叶结点的层数）。

输入描述

例如：由叶子节点 5 15 40 30 10 生成的最优二叉树如下图所示, 该树的最短带权路径长度为 40*1+30*2+15*3+5*4+10*4=205。

输出描述
输出一个哈夫曼的中序遍历数组, 数值间以空格分隔

示例1
输入：
5
5 15 40 30 10

输出：
40 100 30 60 15 30 5 15 10

说明：
根据输入, 生成哈夫曼树, 按照中序遍历返回。所有节点中, 左节点权值小于等于右节点权值之和。当左右节点权值相同时左子树高度小于右子树。结果如上图
"""

import heapq

class TreeNode:
    def __init__(self, weight):
        self.weight = weight
        self.left = None
        self.right = None

    def __lt__(self, other):
        # 定义节点的比较方法，首先比较权值，其次比较高度
        if self.weight == other.weight:
            return self.get_height() < other.get_height()
        return self.weight < other.weight

    def get_height(self):
        if not self.left and not self.right:
            return 1
        left_height = self.left.get_height() if self.left else 0
        right_height = self.right.get_height() if self.right else 0
        return 1 + max(left_height, right_height)

def huffman_tree(weights):
    heap = [TreeNode(w) for w in weights]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = TreeNode(left.weight + right.weight)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def inorder_traversal(root):
    if not root:
        return []
    return inorder_traversal(root.left) + [root.weight] + inorder_traversal(root.right)

def main():
    n = int(input())
    weights = list(map(int, input().split()))
    root = huffman_tree(weights)
    result = inorder_traversal(root)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
