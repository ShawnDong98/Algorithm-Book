class Solution:
    """
        - 建立虚拟头结点
        - first 向后走 n 步
        - first second 同时向后走， 当 first 走到末尾时终止, 此时 second
        走到倒数第 n + 1 个结点
        - 删除倒数第 n 个结点
    """
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        for i in range(n + 1):
            first = first.next
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next
