import sys, heapq

input = sys.stdin.readline


n = int(input())
max_heap = []
for _ in range(n):
    num = int(input())

    heapq.heappush(max_heap, -num)

    if num == 0:
        print(-heapq.heappop(max_heap))

