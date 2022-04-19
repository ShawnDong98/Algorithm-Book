from collections import namedtuple
import heapq as hq


N = 100010

Range = namedtuple('Range', ['l', 'r'])
range_ = []

n = int(input())
for i in range(n):
    l, r = map(int, input().split())
    range_.append(Range(l, r))

range_ = sorted(range_, key=lambda x: x.l)
h = []

for i in range(n):
    r = range_[i]
    if len(h)==0 or h[0] >= r.l: hq.heappush(h, r.r)
    else:
        hq.heappop(h)
        hq.heappush(h, r.r)

print(len(h))

