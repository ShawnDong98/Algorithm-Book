class BSTIterator:

    def __init__(self, root: TreeNode):
        self.queue = collections.deque()
        self.inOrder(root)

    def inOrder(self, root) -> int:
        if not root: return
        self.inOrder(root.left)
        self.queue.append(root.val)
        self.inOrder(root.right)


    def next(self) -> bool:
        return self.queue.popleft()

    def hasNext(self):
        return len(self.queue) > 0
