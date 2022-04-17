import sys
class Solution:
    def check(self, mid, houses, heaters):
        j = 0
        for i in range(len(houses)):
            while j < len(heaters) and abs(heaters[j] - houses[i]) > mid:
                j += 1
            if j >= len(heaters): return False
        return True
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        l = 0
        r = sys.maxsize
        while l < r:
            mid = l + r >> 1
            if self.check(mid, houses, heaters): r = mid
            else: l = mid + 1

        return l
