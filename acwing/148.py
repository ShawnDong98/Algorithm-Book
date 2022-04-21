import heapq

n = int(input())

h = []
inp = list(map(int, input().split()))
for x in inp:
    heapq.heappush(h, x)

res = 0
while(len(h) > 1):
    a = heapq.heappop(h)
    b = heapq.heappop(h)
    res += a + b
    heapq.heappush(h, a + b)

print(res)
