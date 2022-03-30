from collections import defaultdict
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        hash = defaultdict(int)
        for line in wall:
            i = 0
            s = 0
            while i < len(line) - 1:
                s += line[i]
                hash[s] += 1
                i += 1
        res = 0
        for k, v in hash.items():
            res = max(res, v)

        return len(wall) - res
