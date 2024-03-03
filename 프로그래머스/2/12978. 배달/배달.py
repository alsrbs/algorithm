import heapq


def dijkstra(graph, start):
    
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_destination = heapq.heappop(queue) # 탐색 할 노드, 거리를 가져옴.

        if distances[current_destination] < current_distance: # 기존에 있는 거리보다 길다면
            continue

        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance
            
            if distance < distances[new_destination]: # 알고 있는 거리 보다 작으면 갱신
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])

    return distances


def solution(N, road, K):
    
    graph = {i: {} for i in range(1, N+1)}

    for a, b, c in road:

        graph.setdefault(a, {})[b] = min(graph.setdefault(a, {}).get(b, float('inf')), c)
        graph.setdefault(b, {})[a] = min(graph.setdefault(b, {}).get(a, float('inf')), c)

            
    graph1 = dijkstra(graph, 1)
    answer = 0
    for v in graph1.values():
        if v <= K:
            answer += 1
    
    return answer