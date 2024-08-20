"""
题目一:在 O(1)时间内删除链表节点。
给定单向链表的头指针和一个节点指针, 定义一个函数在0(1)时间内删除该节点。链表节点与函数的定义如下:

题目二:删除链表中重复的节点。
在一个排序的链表中, 如何删除重复的节点?例如, 在图 3.4(a)中重复的节点被删除之后, 链表如图3.4(b)所示
"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def delduplicateList(head):
    if head is None or head.next is None:
        return head
    
    dummy = ListNode(0)
    dummy.next = head
    pre = dummy
    current = head

    while current:
        while current.next is not None and current.next.val == current.val:
            current = current.next

        if pre.next == current:
            pre = current
        else:
            pre.next = current.next
        
        current = current.next

    return head

    
