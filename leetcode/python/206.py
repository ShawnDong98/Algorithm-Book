class Solution:
    """
        - c = b->next
        - b ->next = a
        - a = b, b = c
    """
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return None
        a = head
        b = head.next
        while b:
            c = b.next
            b.next = a
            a = b
            b = c

        head.next = None

        return a
