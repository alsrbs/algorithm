from collections import deque

a, b, n, m = map(int, input().split())
graph = [-1]*100001

q = deque([n])
graph[n] = 0

while q:
    l = q.popleft()

    for i in [l-1, l+1, l+a, l+b, l-a, l-b, l*a, l*b]:
        if 0<=i<100001 and graph[i] == -1:
            graph[i] = graph[l]+1
            q.append(i)
            if i==m:
                print(graph[i])
                exit()
