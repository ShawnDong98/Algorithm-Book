class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        p1 = headA
        p2 = headB
        while p1 != p2:
            p1 = headB if p1 is None else p1.next
            p2 = headA if p2 is None else p2.next
        return p1
