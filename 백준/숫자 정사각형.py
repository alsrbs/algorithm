def search():
    for i in range(width, 0, -1):
        for j in range(N):
            for k in range(M):
                if (j+i-1<N and k+i-1<M) and (graph[j][k] == graph[j+i-1][k] == graph[j][k+i-1] == graph[j+i-1][k+i-1]):
                    print(i*i)
                    return

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
width = min(N, M)

if width == 1:
    print(1)
else:
    search()
