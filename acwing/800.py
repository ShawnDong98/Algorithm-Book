n, m, x = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

i = 0
j = m -1
while i< n:
    while j >= 0 and A[i] + B[j] > x:
        j -= 1
    if j >= 0 and A[i] + B[j] == x:
        print(f'{i} {j}')
        break
    i += 1

