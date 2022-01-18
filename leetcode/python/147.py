class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(float("-inf"))
        pre = dummy
        tail = dummy
        cur = head
        while cur:
            if tail.val < cur.val:
                tail.next = cur
                tail = cur
                cur = cur.next
            else:
                tmp = cur.next
                tail.next = tmp
                while pre.next and pre.next.val < cur.val:
                    pre = pre.next
                cur.next = pre.next
                pre.next = cur
                pre = dummy
                cur = tmp

        return dummy.next
