from collections import defaultdict
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        cnt = defaultdict(int)
        for c in nums3:
            for d in nums4:
                cnt[c + d] += 1
        res = 0
        for a in nums1:
            for b in nums2:
                res += cnt[-(a + b)]
        return res

    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        res = []
        for i, a in enumerate(nums1):
            for j, b in enumerate(nums2):
                for k, c in enumerate(nums3):
                    for l, d in enumerate(nums4):
                        if a + b + c + d == 0:
                            res.append([i, j, k, l])

        return len(res)

