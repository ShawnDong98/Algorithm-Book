def quick_search(arr, l, r, k):
    if l >= r: return arr[l]
    i = l - 1
    j = r + 1
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

    if j - l + 1 >= k:
        return quick_search(arr, l, j, k)
    else:
        return quick_search(arr, j + 1, r, k - (j - l + 1))

n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(str(quick_search(arr, 0, n - 1, k)))

