def binary_search(l, r, k):
    while (r - l) > 1e-8:
        mid = (l + r) / 2
        if mid ** 3 >= k:
            r = mid
        else:
            l = mid

    return l

l = -10000
r = 10000
k = float(input())
print(binary_search(l, r, k))