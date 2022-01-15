def findl(x):
    left, right = 0, len(mapping) - 1
    while left < right:
        mid = left + right >> 1
        if mapping[mid] >= x:
            right = mid
        else:
            left = mid + 1
    return left + 1

def findg(x):
    left, right = 0, len(mapping) - 1
    while left < right:
        mid = left + right + 1 >> 1
        if mapping[mid] <= x:
            left = mid
        else:
            right = mid - 1
    return left + 1

n, m = map(int, input().split())
add = [list(map(int , input().split())) for _ in range(n)]
queries = [list(map(int , input().split())) for _ in range(m)]

mapping  = sorted(list(set([v[0] for v in add])))
num = [0] * (len(mapping) + 1)

for pair in add:
    num[findl(pair[0])] += pair[1]

s = [0] * len(num)
for i in range(1, len(s)):
    s[i] = s[i-1] + num[i]

for query in queries:
    begin, end = query
    if begin > mapping[-1] or end < mapping[0]:
        print(0)
    else:
        res = s[findg(end)] - s[findl(begin) - 1]
        print(res)
