N = 100010

q = [0] * N
hh = 0
tt = -1

m = int(input())
for i in range(m):
    inp = input().split()
    if inp[0] == 'push':
        tt += 1
        q[tt] = int(inp[1])
    elif inp[0] == 'pop':
        hh += 1
    elif inp[0] == 'empty':
        if hh <= tt:
            print('NO')
        else:
            print('YES')
    else:
        print(q[hh])

