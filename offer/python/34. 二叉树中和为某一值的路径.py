"""
题目：输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路。
"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root, targetSum):
    def dfs(node, currentPath, currentSum):
        if not node:
            return
        
        currentPath.append(node.val)
        currentSum += node.val

        if not node.left and not node.right and currentSum == targetSum:
            result.append(list(currentPath))

        dfs(node.left, currentPath, currentSum)
        dfs(node.right, currentPath, currentSum)

        currentPath.pop()

    result = []
    dfs(root, [], 0)
    return result



root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

targetSum = 22
print(pathSum(root, targetSum))  # Output: [[5, 4, 11, 2], [5, 8, 4, 5]]