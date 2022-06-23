class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        p = dummy
        while p != None:
            q = p
            i = 0
            while i < k and q:
                q = q.next
                i += 1
            if not q: break
            a = p.next
            b = a.next
            for i in range(k-1):
                c = b.next
                b.next = a
                a = b
                b = c
            c = p.next
            p.next = a
            c.next = b
            p = c

        return dummy.next
