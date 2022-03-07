def get_primes(n):
    global cnt
    for i in range(2, n+1):
        if st[i]: continue
        primes[cnt] = i
        cnt += 1
        j = i + i
        while j <= n:
            st[j] = True
            j += i

N = 1000010
primes = [0] * N
cnt = 0
st = [False] * N

n = int(input())

get_primes(n)

print(cnt)

