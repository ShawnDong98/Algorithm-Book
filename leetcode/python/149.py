from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 0
        for p in points:
            ss = 0
            vs = 0
            cnt = defaultdict(int)
            for q in points:
                if p == q: ss += 1
                elif p[0] == q[0]: vs += 1
                else:
                    k = (q[1] - p[1]) / (q[0] - p[0])
                    cnt[k] += 1
            c = vs
            for k, t in cnt.items(): c = max(c, t)
            res = max(res, c + ss)

        return res

