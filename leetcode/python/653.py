class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def dfs(root, k):
            if not root: return False
            if dfs(root.left, k): return True
            x = root.val
            if hash.get(k-x, False): return True
            hash[x] = True
            return dfs(root.right, k)
        def dfs_v20220212(root, k):
            if not root: return False
            x = root.val
            if hash.get(k-x, False): return True
            hash[x] = True
            return dfs(root.left, k) or dfs(root.right, k)

        hash = {}
        return dfs(root, k)
