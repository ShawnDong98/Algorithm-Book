class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in nums1:
            for idx, j in enumerate(nums2):
                if i == j:
                    res.append(-1)
                    for k in nums2[idx:]:
                        if k > i:
                            res.pop()
                            res.append(k)
                            break

        return res

