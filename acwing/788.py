def merge_sort(arr, left, right, tmp):
    if left >= right: return 0
    mid = left + right >> 1
    res = merge_sort(arr, left, mid, tmp) + merge_sort(arr, mid + 1, right, tmp)

    i = left
    j = mid + 1
    k = 0
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            tmp[k] = arr[i]
            i += 1
            k += 1
        else:
            # 对 a[j] 这个值, a[i] 之后的都是逆序对
            res += mid - i + 1
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

    i = left
    j = 0
    while i <= right:
        arr[i] = tmp[j]
        i += 1
        j += 1

    return res

n = int(input())
arr = list(map(int, input().split()))
tmp = [0] * n
print(merge_sort(arr, 0, n-1, tmp))
