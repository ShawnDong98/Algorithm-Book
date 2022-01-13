from typing import Optional
class Solution:
    """
        - k %= n
        - first 指针从头往后走 k 步
        - second 和 first 同时往后走， 当 first 走到最后一个节点时，结束

    """
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        n = 0
        p = head
        while p:
            n += 1
            p = p.next
        k %= n
        if k == 0: return head
        first = head
        second = head
        while k:
            first = first.next
            k -= 1
        while first.next:
            first = first.next
            second = second.next
        first.next = head
        head = second.next
        second.next = None

        return head


