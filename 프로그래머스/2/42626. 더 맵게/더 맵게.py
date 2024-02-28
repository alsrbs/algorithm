import heapq

def solution(scoville, K):
    
    heapq.heapify(scoville)
    
    result = 0
    while True:
        
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        
        if scoville[0] >= K:
            return result
        
        x1 = heapq.heappop(scoville)
        x2 = heapq.heappop(scoville)
        heapq.heappush(scoville, x1+x2*2)
        result += 1

