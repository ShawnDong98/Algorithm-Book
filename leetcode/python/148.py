from typing import Optional

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(second)
        return self.mergeTwoLists(left, right)

    def mergeTwoLists(self, l1, l2):
        head = cur = ListNode(0)
        while l1 and l2:
            if l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next

        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return head.next
