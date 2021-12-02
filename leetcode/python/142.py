class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        slow = fast = head
        while fast:
            slow = slow.next
            fast = fast.next
            if fast: fast = fast.next
            else: break

            if slow == fast:
                fast = head
                while(fast != slow):
                    fast = fast.next
                    slow = slow.next
                return fast

        return None

