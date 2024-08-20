"""
如果一个链表中包含环，如何找出环的入口节点？
"""

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def find_circle_entry(node):
    if not node:
        return None  

    fast = node
    slow = node

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    else:
        return None
    
    slow = node
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow