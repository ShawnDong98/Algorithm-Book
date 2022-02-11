from typing import List
import collections
class Solution:
    def levelOrder_v20220211(self, root: TreeNode) -> List[List[int]]:
        res = []
        q = collections.deque([])
        if root is not None: q.append(root)
        while q:
            level = []
            l = len(q)

            while l:
                t = q.popleft()
                level.append(t.val)
                if t.left: q.append(t.left)
                if t.right: q.append(t.right)
                l -= 1

            res.append(level)
        return res
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        queue = [root]
        res = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(level)
        return res

