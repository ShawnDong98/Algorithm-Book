class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head: return None
        dummy = ListNode(0)
        dummy.next = head
        count = 1
        pre = dummy
        while pre.next and count < left:
            pre = pre.next
            count += 1
        cur = pre.next
        tail = cur
        while cur and count <= right:
            nxt = cur.next
            cur.next = pre.next
            pre.next = cur
            tail.next = nxt
            cur = nxt
            count += 1

        return dummy.next

