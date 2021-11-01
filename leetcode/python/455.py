from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
            将胃口列表 g 和 饼干列表 s 分别从小到大排序， 设置两个指针 i 和 j。 同时从左到右遍历， 优先满足胃口小的值
        """
        g.sort()
        s.sort()

        count = i = j = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                count += 1
                i += 1
            j += 1

        return count