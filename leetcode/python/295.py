import bisect

class MedianFinder:

    def __init__(self):
        self.l = []


    def addNum(self, num: int) -> None:
        if not self.l:
            self.l.append(num)
        else:
            bisect.insort_left(self.l, num) # 插入

    def findMedian(self) -> float:
        if len(self.l) % 2 == 1:
            return self.l[len(self.l) // 2]
        else:
            return (self.l[len(self.l) // 2] + self.l[len(self.l) // 2 - 1]) / 2 


