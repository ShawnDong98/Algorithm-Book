"""
题目：输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。
"""


class BilListNode:
    def __init__(self, val, pre=None, next=None):
        self.val = val
        self.pre = pre
        self.next = next


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_to_bilist(root):
    if not root:
        return None
    
    def inorder(node):
        nonlocal last, head
        if not node:
            return
        
        inorder(node.left)

        # 如果上一个节点不为 None，上一个节点的 right 指针指向当前节点，当前节点的 left 指针指向上一个节点
        if last:
            last.right = node
            node.left = last
        # last 是否有可能指向最后的 None 节点？
        # head 指向第一个节点
        else:
            head = node

        last = node

        inorder(node.right)

    last, head = None, None
    inorder(root)

    # 构造成一个环？
    if head and last:
        head.left = last
        last.right = head

    return head

# Helper function to print the doubly linked list
def print_doubly_linked_list(head):
    cur = head
    while cur:
        print(cur.val, end=" <-> ")
        cur = cur.right
        if cur == head:
            break
    print("None")

# Example usage:
# Constructing the BST
#        4
#       / \
#      2   5
#     / \
#    1   3
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

# Convert BST to doubly linked list
head = tree_to_bilist(root)

# Print the doubly linked list
print_doubly_linked_list(head)