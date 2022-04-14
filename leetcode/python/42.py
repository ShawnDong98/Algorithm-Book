from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        stk = []
        res = 0
        for i in range(len(height)):
            last = 0
            while len(stk) and height[stk[-1]] <= height[i]:
                res += (height[stk[-1]] - last) * (i - stk[-1] - 1)
                last = height[stk[-1]]
                stk.pop()
            if len(stk): res += (i - stk[-1] - 1) * (height[i] - last)
            stk.append(i)
        return res
    def trap(self, height: List[int]) -> int:
        # 边界条件
        if not height: return 0
        n = len(height)
        maxleft = [0] * n
        maxright = [0] * n
        ans = 0
        # 初始化
        maxleft[0] = height[0]
        maxright[n-1] = height[n-1]
        # 设置备忘录， 分别存储左边和右边最高的柱子高度
        for i in range(1, n):
            maxleft[i] = max(maxleft[i-1], height[i])
        for j in range(n-2, -1, -1):
            maxright[j] = max(maxright[j+1], height[j])
        # 一趟遍历， 比较每个位置可以存储多少水
        for i in range(n):
            if min(maxleft[i], maxright[i]) > height[i]:
                ans += min(maxleft[i], maxright[i]) - height[i]
        return ans
