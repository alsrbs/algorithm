import sys, heapq

input = sys.stdin.readline

n, m = map(int, input().split())
heap = list(map(int, input().split()))

heapq.heapify(heap)

for _ in range(m):
    min_num1 = heapq.heappop(heap)
    min_num2 = heapq.heappop(heap)
    heapq.heappush(heap, min_num1+min_num2)
    heapq.heappush(heap, min_num1 + min_num2)

print(sum(heap))