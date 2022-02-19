class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first = second = last = None
        while root:
            if not root.left:
                if last and last.val > root.val:
                    if not first:
                        first = last
                        second = root
                    else: second = root
                last = root
                root = root.right
            else:
                p = root.left
                while p.right and p.right != root: p = p.right
                if not p.right:
                    p.right = root
                    root = root.left
                else:
                    p.right = None
                    if last and last.val > root.val:
                        if not first:
                            first = last
                            second = root
                        else: second = root
                    last = root
                    root = root.right
        first.val, second.val = second.val, first.val

