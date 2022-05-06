"""
1. 确定分界点： mid = (l + r) / 2
2. 递归排序 left, right
3. 归并—— 合二为一
"""
def merge_sort(arr, left, right, tmp):
    if left >= right: return
    mid = left + right >> 1
    merge_sort(arr, left, mid, tmp)
    merge_sort(arr, mid + 1, right, tmp)
    i = left
    j = mid + 1
    k = 0
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            tmp[k] = arr[i]
            i += 1
        else:
            tmp[k] = arr[j]
            j += 1
        k += 1
    while i <= mid:
        tmp[k] = arr[i]
        i += 1
        k += 1
    while j <= right:
        tmp[k] = arr[j]
        j += 1
        k += 1
    i, j = left, 0
    while i <= right:
        arr[i] = tmp[j]
        i += 1
        j += 1

n = int(input())
arr = list(map(int, input().split()))
tmp = [0] * n
merge_sort(arr, 0, n-1, tmp)
print(' '.join(map(str, arr)))
