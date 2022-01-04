def cmp(A, B):
    if (len(A) != len(B)): return len(A) > len(B)

    for i in range(len(A) - 1, -1, -1):
        if A[i] != B[i]: return A[i] > B[i]

    return True

def sub(A, B):
    C = []
    t = 0 
    for i in range(len(A)):
        t = A[i] - t
        if (i < len(B)): t -= B[i]
        C.append((t + 10) % 10)
        if (t < 0): t = 1
        else: t = 0
    
    while(len(C) > 1 and C[-1] == 0): C.pop()
    return C

a = str(input())
b = str(input())
A, B  = [], []
for i in range(len(a) - 1, -1, -1): A.append(int(a[i]))
for i in range(len(b) - 1, -1, -1): B.append(int(b[i]))

if cmp(A, B): 
    C = sub(A, B)
else: 
    C = sub(B, A) 
    print('-', end='')

for i in range(len(C) - 1, -1, -1):
    print(C[i], end='')

