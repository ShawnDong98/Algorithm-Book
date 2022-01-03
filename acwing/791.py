def add(A, B):
    if len(A) < len(B): return add(B, A)
    
    C = []
    t = 0
    for i in range(len(A)):
        t += A[i]
        if i < len(B):
            t += B[i]
        C.append(t % 10)
        t //= 10

    if t: C.append(t)
    return C

a = str(input())
b = str(input())
A, B = [], []
for i in range(len(a)-1, -1, -1): A.append(int(a[i]))
for i in range(len(b)-1, -1, -1): B.append(int(b[i]))

C = add(A, B)
for i in range(len(C)-1, -1, -1):
    print(C[i], end='')

