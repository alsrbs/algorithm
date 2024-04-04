import heapq

operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]

max_h = []
min_h = []

for i in operations:
    operation, n = i.split()

    if operation == 'I':
        heapq.heappush(min_h, int(n))
        heapq.heappush(max_h, (-int(n), int(n)))
        continue

    try:
        if n == '1':
            max_val = heapq.heappop(max_h)[1]
            min_h.remove(max_val)
        else:
            min_val = heapq.heappop(min_h)
            max_h.remove((-min_val, min_val))
    except:
        pass

if min_h:
    print(heapq.heappop(max_h)[1], heapq.heappop(min_h))
else:
    print(0, 0)

