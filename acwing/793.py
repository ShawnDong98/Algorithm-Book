def multiply(A, b):
    C = []
    t = 0
    i = 0
    while t != 0 or i < len(A):
        if i < len(A): 
            t += A[i] * b
            i += 1
        C.append(t % 10)
        t //= 10
    
    while(len(C) > 1 and C[-1] == 0): C.pop()
    return C


a = str(input())
b = int(input())

A = []

for i in range(len(a)-1, -1, -1): A.append(int(a[i]))

C = multiply(A, b)

for i in range(len(C)-1, -1, -1): print(C[i], end='')

