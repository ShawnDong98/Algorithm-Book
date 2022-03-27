import collections
from typing import List

class Solution:
    def findDuplicateSubtrees_v20220327(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def dfs(root):
            nonlocal cnt
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            key = str(root.val) + ' ' + str(left) + ' ' + str(right)
            if key not in ids:
                cnt += 1
                ids[key] += cnt
            id = ids[key]
            hash[id] += 1
            if hash[id] == 2:
                ans.append(root)
            return id

        ids = collections.defaultdict(int)
        cnt = 0
        hash = collections.defaultdict(int)
        ans = []

        dfs(root)
        return ans


    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.map[key] = -1
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
