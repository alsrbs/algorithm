import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
vis = [0]*(n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

stack = [[1, 0]]
ans = []
while stack:
    a, c = stack.pop()
    vis[a] = 1

    if a != 1 and len(graph[a]) == 1:
        ans.append(c)
        continue

    for i in graph[a]:
        if vis[i] == 0:
            stack.append([i, c + 1])

if sum(ans)%2 == 1:
    print('Yes')
else:
    print('No')