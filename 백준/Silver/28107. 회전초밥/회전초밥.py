import sys, heapq

input = sys.stdin.readline


n, m = map(int, input().split())
order = [[] for _ in range(200001)]

for i in range(n):
    k = list(map(int, input().split()))
    for j in k[1:]:
        heapq.heappush(order[j], i)

menu = list(map(int, input().split()))
result = [0]*n
for i in menu:
    if order[i]:
        x = heapq.heappop(order[i])
        result[x] += 1

print(*result)