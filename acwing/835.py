def insert(s):
    global idx
    p = 0
    for i in range(len(s)):
        u = ord(s[i]) - ord('a')
        if not son[p][u]:
            idx += 1
            son[p][u] = idx
        p = son[p][u]
    cnt[p] += 1

def query(s):
    p = 0
    for i in range(len(s)):
        u = ord(s[i]) - ord('a')
        if not son[p][u]:
            return 0
        p = son[p][u]
    return cnt[p]

N = 100010
n = int(input())
son = [[0] * 26 for i in range(N)]
cnt = [0] * N
idx = 0


for i in range(n):
    inp = input().split()
    if inp[0] == 'I':
        insert(inp[1])
    if inp[0] == 'Q':
        print(query(inp[1]))
