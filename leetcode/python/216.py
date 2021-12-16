from typing import List
class Solution:
    """
    依次枚举每个数从哪个位置上选

    dfs(枚举到了第几个数字， 开始枚举的位置， 当前选择的所有数的和)
    """
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        path = []
        used = [False] * 10
        res = []

        def back_trace(idx, total):
            if total == n and len(path) == k:
                res.append(path[:])
                return
            if total > n or idx == 10 or (not path and idx * k > n):
                return
            for i in range(idx, 10):
                if not used[i]:
                    used[i] = True
                    path.append(i)
                    back_trace(i + 1, total + i)
                    used[i] = False
                    path.pop()

        back_trace(1, 0)
        return res

k = 9
n = 45
S = Solution()
print(S.combinationSum3(k, n))
