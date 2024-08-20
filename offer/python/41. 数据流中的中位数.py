"""
题目： 如何得到一个数据流中的中位数？如果从数据流中读出奇数个数, 那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数, 那么中位数就是所有数值排序之后中间两个数的平均值。
"""
import heapq

def func(inp):
    inp = sorted(inp)
    print(inp)
    idx = len(inp) // 2 - 1
    if len(inp) % 2 == 0:
        res = (inp[idx] + inp[idx+1]) / 2
    else:
        res = inp[idx]

    return res

class MedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num):
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self):
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        
        else:
            return -self.max_heap[0]




inp = [1, -2, 3, 10, -4, 7, 2, -5]
print(func(inp))

# 示例用法
medianFinder = MedianFinder()
nums = [1, -2, 3, 10, -4, 7, 2, -5]
for num in nums:
    medianFinder.addNum(num)
    print("当前数据流中的中位数是：", medianFinder.findMedian())