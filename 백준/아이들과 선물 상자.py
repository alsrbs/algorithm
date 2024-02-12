import sys, heapq

input = sys.stdin.readline


n, m = map(int, input().split())  # 선물 수, 아이들 수
gift = list(map(int, input().split()))
children = list(map(int, input().split()))

gift = [-i for i in gift]
heapq.heapify(gift)

result = False
for i in range(m):
    if -gift[0] < children[i]:
        result = True
        break
    heapq.heapreplace(gift, -(-gift[0] - children[i]))

if result:
    print(0)
else:
    print(1)