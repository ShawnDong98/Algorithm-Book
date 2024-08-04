"""
题目:给定一棵二叉树和其中的一个节点，如何找出中序遍历序列的下一个节点?树中的节点除了有两个分别指向左、右子节点的指针，还有一个指向父节点的指针。

"""

class TreeNode:
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None

    def next_node(self, node):
        if not node:
            return None
        
        if node.right:
            node = node.right
            while node.left:
                node = node.left    
            return node
        
        while node.parent and node == node.parent.right:
            node = node.parent

        return node
        

