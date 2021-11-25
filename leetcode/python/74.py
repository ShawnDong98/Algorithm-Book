from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        def binary_search(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return True
                if nums[mid] > target:
                    right = mid
                else:
                    left = mid + 1
            return False

        for row in matrix:
            if binary_search(row, target):
                return True
        return False


matix = [[1, 3, 5]]
S = Solution()
print(S.searchMatrix(matix, 1))
