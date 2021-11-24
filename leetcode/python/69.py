class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        low, high = 1, x
        while low <= high:
            mid = (low + high) // 2
            if  mid < x / mid:
                low = mid + 1
            elif mid > x / mid:
                high = mid - 1
            else:
                return mid
        return high



