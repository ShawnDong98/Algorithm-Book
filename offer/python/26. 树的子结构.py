"""
输入两棵二叉树 A 和 B 判断 B 是不是 A 的子结构

第⼀步在树 A 中查找与根节点的值⼀样的节点, 这实际上就是树的遍历

第⼆步是判断树A中以 R 为根节点的⼦树是不是和树B具有相同的结构 
"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSubStructure(tree1, tree2):
    if not tree1 or not tree2:
        return False
    
    def is_match(tree1, tree2):
        if not tree2:
            return True
        if not tree1 or tree1.val != tree2.val:
            return False
        return is_match(tree1.left, tree2.left) and is_match(tree1.right, tree2.right)


    return is_match(tree1, tree2) or isSubStructure(tree1.left, tree2) or isSubStructure(tree1.right, tree2)

        

# 测试用例
# 创建二叉树 A
A = TreeNode(3)
A.left = TreeNode(4)
A.right = TreeNode(5)
A.left.left = TreeNode(1)
A.left.right = TreeNode(2)

# 创建二叉树 B
B = TreeNode(4)
B.left = TreeNode(1)

# 判断 B 是否是 A 的子结构
print(isSubStructure(A, B))  # 输出 True