"""
题目：输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
"""

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def merge_linked_list(linklist1, linklist2):
    if not linklist1 and not linklist2:
        return None
    if not linklist1 and linklist2:
        return linklist2
    if linklist1 and not linklist2:
        return linklist1
    
    dummy = ListNode(0)
    current = dummy

    while linklist1 and linklist2:
        if linklist1.val < linklist2.val:
            current.next = linklist1
            linklist1 = linklist1.next
        else:
            current.next = linklist2
            linklist2 = linklist2.next

        current = current.next

    if linklist1:
        current.next = linklist1
    
    if linklist2:
        current.next = linklist2

    return dummy.next
        
        

# 辅助函数，用于创建链表和打印链表
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# 示例
l1 = create_linked_list([1, 2, 4])
l2 = create_linked_list([1, 3, 4])
merged_list = merge_linked_list(l1, l2)
print_linked_list(merged_list)