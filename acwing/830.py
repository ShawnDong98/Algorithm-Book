N = 100010
stk = [0] * N
tt = 0
arr = list(map(int, input().split()))

n = int(input())
for x in arr:
    while tt and stk[tt] >= x: tt -= 1
    if not tt: print("-1 ")
    else: print(stk[tt])
    tt += 1
    stk[tt] = x
