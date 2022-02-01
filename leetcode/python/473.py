from typing import List

class Solution:
    def makesquare_v20220201(self, nums: List[int]) -> bool:
        def dfs(start, cur, length, cnt):
            if cnt == 3: return True
            if cur == length: return dfs(0, 0, length, cnt + 1)
            for i in range(start, len(nums)):
                if st[i]: continue
                if cur + nums[i] <= length:
                    st[i] = True
                    if dfs(i + 1, cur + nums[i], length, cnt): return True
                    st[i] = False
                if not cur or cur + nums[i] == length: return False
                while i +  1 < len(nums) and nums[i+1] == nums[i]:
                    i += 1
            return False
        if not len(nums): return False
        st = [False] * len(nums)
        sum = 0
        for x in nums: sum += x
        if sum % 4: return False
        sum //= 4
        sorted(nums, reverse=True)
        return dfs(0, 0, sum, 0)
    def makesquare(self, nums: List[int]) -> bool:
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


