from collections import namedtuple

N = 100010
n = int(input())
Range = namedtuple('Range', ['l', 'r'])
range_ = []

for i in range(n):
    l, r = map(int, input().split())
    range_.append(Range(l, r))

    range_ = sorted(range_, lambda x: x.r)

    res = 0
    ed = -2e9
    for i in range(n):
        if ed < range_[i].l:
            res += 1
            ed = range_[i].r

    print(res)

