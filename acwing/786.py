def quick_search(arr, left, right, k):
    if left >= right: return arr[left]
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

    # 左侧总共有多少个数
    sl = j - left + 1

    # 如果k在左侧
    if k <= sl:
        return quick_search(arr, left, j, k)
    # 如果k在右侧，那么要找的数是右侧的第 k - sl 小的数
    else:
        return quick_search(arr, j+1, right, k - sl)

n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(str(quick_search(arr, 0, n-1, k)))
