import heapq


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_destination = heapq.heappop(queue) # 탐색 할 노드, 거리를 가져옴.

        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])

    return distances


N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3

graph = {i: {} for i in range(1, N+1)}

for a, b, c in road:

    graph.setdefault(a, {})[b] = min(graph.setdefault(a, {}).get(b, float('inf')), c)
    graph.setdefault(b, {})[a] = min(graph.setdefault(b, {}).get(a, float('inf')), c)


graph1 = dijkstra(graph, 1)
answer = 0
for v in graph1.values():
    if v <= K:
        answer += 1

print(answer)
