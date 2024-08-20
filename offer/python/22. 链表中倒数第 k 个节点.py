"""
题目：输入一个链表，输出该链表中倒数第 k 个节点。为了符合大多数人的习惯，本题从 1 开始计数，即链表的尾节点是倒数第 1 个节点。


例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点
"""

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def find_kth_from_end(node, k):
    if not node:
        return None
    
    fast = node
    slow = node
    
    for i in range(k):
        if fast == None:
            return None
        fast = fast.next

    while fast:
        fast = fast.next
        slow = slow.next

    return slow


node6 = ListNode(6)
node5 = ListNode(5, node6)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
head = ListNode(1, node2)

k = 3
result = find_kth_from_end(head, k)
if result:
    print(f"倒数第 {k} 个节点的值是: {result.val}")
else:
    print("链表长度小于 k")

