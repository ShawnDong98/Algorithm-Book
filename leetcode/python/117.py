class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        cur = root
        while cur:
            head = Node(-1)
            tail = head
            p = cur
            while p:
                if p.left:
                    tail.next = p.left
                    tail = tail.next
                if p.right:
                    tail.next = p.right
                    tail = tail.next
                p = p.next
            cur = head.next
        return root

