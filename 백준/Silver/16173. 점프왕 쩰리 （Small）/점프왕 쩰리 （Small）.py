from collections import deque


def bfs():
    vis = [[0]*n for _ in range(n)]
    vis[0][0] = 1
    q = deque([(0, 0)])

    while q:
        r, c = q.popleft()
        jump = graph[r][c]

        for i in [(0, jump), (jump, 0)]:
            nr = r + i[0]
            nc = c + i[1]

            if 0 <= nr < n and 0 <= nc < n and vis[nr][nc] == 0:
                vis[nr][nc] = 1
                q.append((nr, nc))

                if graph[nr][nc] == -1:
                    return 'HaruHaru'

    return 'Hing'


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
print(bfs())