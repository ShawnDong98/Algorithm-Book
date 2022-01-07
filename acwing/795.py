n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
pre_sum = [0] * len(arr)

for i in range(1, n+1):
    pre_sum[i] = pre_sum[i-1] + arr[i]

for _ in range(m):
    l, r = map(int, input().split())
    print(pre_sum[r] - pre_sum[l-1])

