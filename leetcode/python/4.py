class Solution:
    def find(self, nums1, i, nums2, j, k):
        if (len(nums1) - i > len(nums2) - j): return self.find(nums2, j, nums1, i, k)
        if k == 1:
            if len(nums1) == i: return nums2[j]
            else: return min(nums1[i], nums2[j])
        if len(nums1) == i: return nums2[j + k - 1]
        si = min(len(nums1), i + k // 2)
        sj = j + k - k // 2
        if nums1[si-1] > nums2[sj-1]:
            return self.find(nums1, i, nums2, sj, k-(sj-j))
        else:
            return self.find(nums1, si, nums2, j, k-(si-i))

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        tot = len(nums1) + len(nums2)
        if tot % 2 == 0:
            left = self.find(nums1, 0, nums2, 0, tot // 2)
            right = self.find(nums1, 0, nums2, 0, tot // 2 + 1)
            return (left + right) / 2
        else:
            return self.find(nums1, 0, nums2, 0, tot // 2 + 1)


