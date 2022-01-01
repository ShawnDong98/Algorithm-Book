def binary_search(arr, k):
    l = 0
    r = len(arr) - 1

    while l < r:
        mid = (l + r) // 2
        if arr[mid] >= k:
            r = mid
        else:
            l = mid + 1
    if arr[l] != k:
        return [-1, -1]

    left = l

    l = 0
    r = len(arr) - 1
    while l < r:
        mid = (l + r + 1) // 2
        if arr[mid] <= k:
            l = mid
        else:
            r = mid - 1

    return [left, l]

n, q = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(q):
    k = int(input())
    res = binary_search(arr, k)
    print(' '.join(map(str, res)))