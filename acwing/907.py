from collections import namedtuple

N = 100010

Range = namedtuple("Range", ["l", "r"])
range_ = []

st, ed = map(int, input().split())
n = int(input())

for i in range(n):
    l, r = map(int, input().split())
    range_.append(Range(l, r))

range_ = sorted(range_, lambda x: x.l)

res = 0
success = False
for i in range(n):
    j = i
    r = -2e9
    while j < n and range_[j].l <= st:
        r = max(r, range_[j].r)
        j += 1

    if r < st:
        res = -1
        break

    res += 1
    if r >= ed:
        success = True
        break

    st = r
    i = j - 1

if not success: res = -1
print(res)
