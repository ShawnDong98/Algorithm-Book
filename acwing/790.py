def binary_search(l, r, n):
    while l < r:
        mid = (l + r) / 2
        if mid ** 3 > n: r = mid
        else l = mid
    return l
l = -10000
r = 10000
n = float(input())
print("{:.6f}".format(binary_search(l, r, n))
