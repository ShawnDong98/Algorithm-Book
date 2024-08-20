"""
题目： 输入 n 个整数，找出其中最小的 k 个数。例如，输入 4, 5, 1, 6, 2, 7, 3, 8 这 8 个数字，则最小的 4 个数字是 1, 2, 3, 4。
"""

def func(inp, k):
    inp = sorted(inp)
    return inp[:k]

def func1(inp, left, right, k):
    if left >= right: return inp[left]
    i = left
    j = right
    x = inp[i + j >> 1]

    while i < j:
        while inp[i] < x:
            i += 1
        while inp[j] > x:
            j -= 1

        if i < j:
            inp [i], inp[j] = inp[j], inp[i]

    sl = j - left + 1

    if sl >= k: func1(inp, left, j, k)
    else: func1(inp, j+1, right, k-sl)

    return inp[:k]

 




inp = [4, 5, 1, 6, 2, 7, 3, 8]
k = 4

print(" ".join(map(str, func(inp, k))))
print(" ".join(map(str, func1(inp, 0, len(inp)-1, k))))