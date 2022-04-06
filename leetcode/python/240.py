class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0: return False
        n, m = len(matrix), len(matrix[0])
        i = 0
        j = m - 1
        while i < n and j >= 0:
            t = matrix[i][j]
            if t == target: return True
            elif t > target: j -= 1
            else: i += 1
        return False
