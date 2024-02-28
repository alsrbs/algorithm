import heapq

scoville = [1, 2, 3, 9, 10, 12]
k = 7

heapq.heapify(scoville)
result = 0
while True:

    if len(scoville) == 1 and scoville[0] < k:
        result = -1
        break
    if scoville[0] >= k:
        break
    x1 = heapq.heappop(scoville)
    x2 = heapq.heappop(scoville)
    heapq.heappush(scoville, x1+x2*2)

    result += 1

print(result)