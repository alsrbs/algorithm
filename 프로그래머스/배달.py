from collections import deque

N = 6
road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
K = 4

graph = [[0]*(N+1) for _ in range(N+1)]
graph2 = [[] for _ in range(N+1)]

for i in range(len(road)):

    graph2[road[i][0]].append(road[i][1])

    if graph[road[i][0]][road[i][1]] == 0:
        graph[road[i][0]][road[i][1]] = road[i][2]
        graph[road[i][1]][road[i][0]] = road[i][2]
    else:
        graph[road[i][0]][road[i][1]] = min(graph[road[i][0]][road[i][1]], road[i][2])
        graph[road[i][1]][road[i][0]] = min(graph[road[i][1]][road[i][0]], road[i][2])

print(graph2)

result = []
for i in graph2[1]:

    q = deque([i])

    j = 1
    while q:
        x = q.popleft()
        graph[j][x]
        result.append(x)
        q += graph2[x]
        j = x

print(result)