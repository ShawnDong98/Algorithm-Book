from typing import List

class Solution:
    """
        二分的流程:
            - 确定二分的边界
            - 编写二分的代码框架
            - 设计一个check(性质)
            - 判断一下区间如何更新
            - 如果更新方式写的是 l = mid, r = mid - 1，
            那么就在计算 mid 的时候加上1
    """
    def hIndex(self, citations: List[int]) -> int:
        l = 0
        r = len(citations)
        while l < r:
            m = 1 + (l + r) // 2
            if citations[len(citations) - m] >= m:
                l = m
            else:
                r = m - 1
        return r
