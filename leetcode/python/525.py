class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        hash = defaultdict(int)
        hash[0] = 0
        res = 0
        one = 0
        zero = 0
        for i in range(1, n+1):
            x = nums[i-1]
            if x == 0: zero += 1
            else: one += 1

            s = one - zero
            if s in hash: res = max(res, i - hash[s])
            else: hash[s] = i

        return res
