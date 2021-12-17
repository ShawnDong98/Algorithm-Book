from typing import List

class Solution:
    """
    依次构造正方形的每条边
    剪枝：
    - 从大到小枚举所有边
    - 每条边内部的木棒长度规定成从大到小
    - 如果当前木棒拼接失败， 则跳过接下来所有长度相同的木棒
    - 如果当前木棒拼接失败， 且是当前边的第一个， 则直接剪掉当前分支
    - 如果当前木棒拼接失败， 切实当前边的最后一个， 则直接减到当前分支

    首先要满足能被4整除
    然后用回溯是否能找到4个边长相等的组成的火柴棒
    """
    def makesquare(self, nums: List[int]) -> bool:
        if len(nums) < 4: return False
        div, mod = divmod(sum(nums), 4)
        if mod != 0:
            return False

        c = collections.Counter(nums)

        def dfs(cnt, edges):
            if edges == 0:
                if cnt == 0:
                    return True
                return dfs(cnt - 1, div)
            for k in c:
                if c[k] > 0 and k <= edges:
                    c[k] -= 1
                    if dfs(cnt, edges - k):
                        return True
                    c[k] += 1
            return False
        return dfs(3, div)


