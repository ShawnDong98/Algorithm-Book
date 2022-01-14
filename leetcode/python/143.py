class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        - 快慢指针找重点，等分成左右两个部分
        - 右半部分逆序
        - 左右两个部分逐个拼接
        """
        def reverseList(node: ListNode):
            pre = None
            cur = node
            while cur:
                temp = cur.next
                cur.next = pre
                pre = cur
                cur = temp
            return pre

        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next

        reverse_node = slow.next
        right = reverseList(reverse_node)
        slow.next = None
        left = head

        while right:
            left = left.next
            head.next = right
            head = head.next
            right = right.next
            head.next = left
            head = head.next


