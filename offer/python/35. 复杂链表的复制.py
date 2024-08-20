"""
题目：请实现函数 ComplexListNode* Clone(ComplexListNode* pHead)，复制一个复杂链表。在复杂链表中，每个节点除了有一个 m_pNext 指针指向下一个节点，还有一个 m_pSibling 指针指向链表中的任意节点或者 nullptr。
"""

class ComplexListNode:
    def __init__(self, val, m_pnext=None, m_pSibling=None):
        self.val = val
        self.m_pnext = m_pnext
        self.m_pSibling = m_pSibling


def Clone(phead):
    if not phead:
        return None
    
    # 在原节点后面创建新节点
    current = phead
    while current:
        temp = ComplexListNode(current.val)
        temp.m_pnext = current.m_pnext
        current.m_pnext = temp
        current = temp.m_pnext

    # 复制任意指针
    current = phead
    while current:
        if current.m_pSibling:
            current.m_pnext.m_pSibling = current.m_pSibling.m_pnext
        current = current.m_pnext.m_pnext

    # 分离两个子链表
    current = phead
    new_head = phead.m_pnext
    while current:
        clone_node = current.m_pnext
        current.m_pnext = clone_node.m_pnext
        if clone_node.m_pnext:
            clone_node.m_pnext = clone_node.m_pnext.m_pnext
        current = current.m_pnext

    return new_head



def print_list(head):
    current = head
    while current:
        sibling_value = current.m_pSibling.val if current.m_pSibling else None
        print(f"Node value: {current.val}, Sibling value: {sibling_value}")
        current = current.m_pnext

# 创建一个复杂链表进行测试
node1 = ComplexListNode(1)
node2 = ComplexListNode(2)
node3 = ComplexListNode(3)
node4 = ComplexListNode(4)

node1.m_pnext = node2
node2.m_pnext = node3
node3.m_pnext = node4

node1.m_pSibling = node3
node2.m_pSibling = node1
node4.m_pSibling = node2

# 打印原始链表
print("Original list:")
print_list(node1)

# 复制链表
cloned_head = Clone(node1)

# 打印复制的链表
print("\nCloned list:")
print_list(cloned_head)

