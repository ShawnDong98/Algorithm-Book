def merge_sort(arr, l, r, tmp):
    if l >= r: return
    mid = (l + r) // 2
    merge_sort(arr, l, mid, tmp)
    merge_sort(arr, mid + 1, r, tmp)
    i = l
    j = mid + 1
    k = 0
    while (i <= mid and j <= r):
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
    while j <= r:
        tmp[k] = arr[j]
        j += 1
        k += 1
    i, j = l, 0
    while i <= r:
        arr[i] = tmp[j]
        i += 1
        j += 1

n = int(input())
arr = list(map(int, input().split()))
tmp = [0] * n
merge_sort(arr, 0, n - 1, tmp)
print(' '.join(map(str, arr)))




