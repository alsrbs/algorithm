from collections import deque
import sys

input = sys.stdin.readline


def bfs(v):
    global count

    q = deque([v])
    vis_t[v] = 0
    vis_d[v] = 1

    while q:
        x = q.popleft()

        for i in sorted(graph[x]):

            if not vis_d[i]:
                count += 1
                vis_d[i] = count
                q.append(i)

            if vis_t[i] == -1:
                vis_t[i] = vis_t[x] + 1


n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
vis_d = [0] * (n+1)
vis_t = [-1] * (n+1)
count = 1

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

bfs(r)

result = 0
for i in range(1, n+1):
    result += vis_t[i]*vis_d[i]

print(result)