class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or head.next == None:
            return False

        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
