"""
题目一：不分行从上到下打印二叉树

从上到下打印出二叉树的每个节点, 同一层的节点按照从左到右的顺序打印。例如, 输入图 4.6 中的二叉树, 则依次打印出 8, 6, 10, 5, 7, 9, 11。

题目二：

从上到下按层打印二叉树, 每一层打印到一行。

题目三：

要求按照之字形(Zigzag) 顺序打印二叉树, 即第一行从左到右打印, 第二行从右到左打印, 第三行再从左到右打印, 以此类推。
"""
from collections import deque
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs(root):
    if not root:
        return None
    
    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.val, end=" ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def bfs1(root):
    if not root:
        return None
    
    queue = deque([root])

    
    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):

            node = queue.popleft()

            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        print(" ".join(map(str, current_level)))


def bfs2(root):
    if not root:
        return None
    
    queue = deque([root])

    cnt = 0
    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):

            node = queue.popleft()

            current_level.append(node.val)

            if cnt % 2 == 1:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
                
        print(" ".join(map(str, current_level)))


root = TreeNode(8)
root.left = TreeNode(6)
root.right = TreeNode(10)
root.left.left = TreeNode(5)
root.left.right = TreeNode(7)
root.right.left = TreeNode(9)
root.right.right = TreeNode(11)

bfs(root)  # 输出: 8 6 10 5 7 9 11
print()
bfs1(root)
bfs2(root)

