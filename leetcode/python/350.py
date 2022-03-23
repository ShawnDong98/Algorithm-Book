class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        res = []
        for num in nums1:
            if num in nums2:
                res.append(num)
                nums2.remove(num)
        return res

