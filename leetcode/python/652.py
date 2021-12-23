from typing import List

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        hash = collections.defaultdict(int)
        count = collections.defaultdict(int)
        self.cnt = 0

        hash['#'] += self.cnt
        self.cnt += 1
        res = []

        def dfs(root):
            if not root:
                return str(hash['#'])
            left, right = dfs(root.left), dfs(root.right)
            subtree = str(root.val) + ',' + left + ',' + right

            if subtree not in hash:
                hash[subtree] += self.cnt
                self.cnt += 1
            t = hash[subtree]
            count[t] += 1

            if count[t] == 2:
                res.append(root)
            return str(t)

        dfs(root)
        return res
