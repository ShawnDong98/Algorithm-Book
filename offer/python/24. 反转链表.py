"""
题目：定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
"""

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    

def reverse_linklist(head):
    if not head:
        return None
    
    pre = None
    current = head

    while current:
        temp = current.next
        current.next = pre
        pre = current
        current = temp
    
    return pre


def print_linked_list(head):
    current = head
    while current is not None:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# 创建一个链表 1 -> 2 -> 3 -> 4 -> None
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

print("Original linked list:")
print_linked_list(head)

# 反转链表
reversed_head = reverse_linklist(head)

print("Reversed linked list:")
print_linked_list(reversed_head)

        

