from collections import defaultdict
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = [0] * (n + 1)
        for i in range(1, n + 1):
            s[i] = s[i - 1] + nums[i - 1]
        hash = defaultdict(int)
        hash[0] = 1
        res = 0
        for i in range(1, n + 1):
            res += hash[s[i] - k]
            hash[s[i]] += 1

        return res

    def subarraySum(self, nums: List[int], k: int) -> int:
    """
    - 遍历，计算从索引0开始到当前位置的所有子串和total，并将该和的出现次数存入哈希表count中
    - 在遍历过程中，若子串和为k，数量res + 1
    - 若当前子串和total减去k在哈希表中出现过，数量res + 该差值出现的次数

    比如前面几个数字相加和为x，再加上后面几个数以后和变成x + k = total，说明从和为x的数到当前数之间的数和为k，
    所以相应的次数res要增加，此时的情况就是 total - k = x 这个x在之前已出现过，且出现过几次res就增加几
    """
        total = 0
        res = 0
        count = {}
        for num in nums:
            total += num
            if total == k:
                res += 1
            if total - k in count:
                res += count[total - k]
            count[total] = count.get(total, 0) + 1

        return res

# nums = [1, -1, 0]
nums = [0, 0]
k = 0
S = Solution()
print(S.subarraySum(nums, k))
