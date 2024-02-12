import sys, heapq

input = sys.stdin.readline


n, k = map(int, input().split())
position = [[] for _ in range(12)]

for _ in range(n):
    p, w = map(int, input().split())
    heapq.heappush(position[p], -w)


for _ in range(k):
    for i in range(1, 12):
        if position[i]:
            if -position[i][0] > 0:
                heapq.heapreplace(position[i], position[i][0]+1)


result = 0
for i in range(1, 12):
    if position[i]:
        result += -position[i][0]

print(result)