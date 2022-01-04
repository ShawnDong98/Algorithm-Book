from typing import List
class SummaryRanges:

    def __init__(self):
        self.res = []

    def addNum(self, val: int) -> None:
        if val not in self.res:
            self.res.append(val)
            self.res.sort()

    def getIntervals(self) -> List[List[int]]:
        out = []
        left = self.res[0]
        for i in range(1, len(self.res)):
            if self.res[i] == self.res[i-1] + 1:
                continue
            else:
                out.append([left, self.res[i-1]])
                left = self.res[i]
        out.append([left, self.res[-1]])
        return out