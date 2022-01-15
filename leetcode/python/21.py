class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        p1 = list1
        p2 = list2
        dummy = head = ListNode(0)
        while p1 != None and p2 != None:
            if p1.val < p2.val:
                head.next = p1
                p1 = p1.next
            else:
                head.next = p2
                p2 = p2.next
            head = head.next
        while p1 != None:
            head.next = p1
            p1 = p1.next
            head = head.next
        while p2 != None:
            head.next = p2
            p2 = p2.next
            head = head.next

        return head.next
