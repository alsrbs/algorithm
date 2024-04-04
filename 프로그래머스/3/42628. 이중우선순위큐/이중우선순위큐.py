import heapq

def solution(operations):
    max_h = []
    min_h = []
    
    for i in operations:
        operation, n = i.split()

        if operation == 'I':
            heapq.heappush(min_h, int(n))
            heapq.heappush(max_h, (-int(n), int(n)))
            continue
            
        if len(min_h) == 0:continue
        
        if n == '1':
            max_val = heapq.heappop(max_h)[1]
            min_h.remove(max_val)
        else:
            min_val = heapq.heappop(min_h)
            max_h.remove((-min_val, min_val))
            
    if min_h:
        return [heapq.heappop(max_h)[1], heapq.heappop(min_h)]
    else:
        return [0, 0]
