import sys, heapq

input = sys.stdin.readline


n, h, t = map(int, input().split())
heap = [-int(input()) for _ in range(n)]
heapq.heapify(heap)

cnt = 0
for _ in range(t):

    if -heap[0] == 1 or -heap[0] < h:
        break
    else:
        heapq.heapreplace(heap, -(-heap[0] // 2))
        cnt += 1


if -heap[0] >= h:
    print('NO', -heap[0], sep='\n')
else:
    print('YES', cnt, sep='\n')
