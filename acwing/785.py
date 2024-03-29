def quick_sort(arr, left, right):
    if left >= right: return

    i = left - 1
    j = right + 1
    x = arr[(i + j) // 2]
    while i < j:
        while True:
            i += 1
            if arr[i] >= x: break
        while True:
            j -= 1
            if arr[j] <= x: break

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    quick_sort(arr, left, j)
    quick_sort(arr, j+1, right)

n = int(input())
arr = list(map(int, input().split()))
quick_sort(arr, 0, n-1)
print(' '.join(map(str, arr)))
