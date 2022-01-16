n = int(input())
arr = []
for i in range(n):
    l, r = map(int, input().split())
    arr.append((l, r))

arr = sorted(arr, key=lambda x: x[0])

st, ed = arr[0]
res = []
for st_, ed_ in arr[1:]:
    if st_ <= ed:
        st = st
        ed = max(ed, ed_)
    if st_ > ed:
        res.append((st, ed))
        st = st_
        ed = ed_
res.append((st, ed))

print(len(res))

