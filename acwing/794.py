def div(A, b):
    C = []
    r = 0
    for i in range(len(A)-1, -1, -1): 
        r = r * 10 + A[i]
        print(r)
        C.append(r // b)
        r %= b

    C = C[::-1]

    while(len(C) > 1 and C[-1] == 0): C.pop()
    return C, r

a = input()
b = int(input())

A  = []

for i in range(len(a)-1, -1, -1): A.append(int(a[i]))

C, r = div(A, b)


for i in range(len(C)-1, -1, -1): print(C[i], end='')

print(r)