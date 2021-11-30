class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head: return None
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next = b
            a.next = b.next
            b.next = a
            pre = a

        return dummy.next
