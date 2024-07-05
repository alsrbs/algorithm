from collections import deque


def bfs(x, y):
    q = deque([(x, y, 0)])  # (x, y, 현재까지 거리)
    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True

    gram_distance = float('inf')
    end_distance = float('inf')

    while q:
        r, c, cnt = q.popleft()

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and graph[nr][nc] != 1:
                visited[nr][nc] = True

                if graph[nr][nc] == 2:
                    gram_distance = cnt + 1 + (n - 1 - nr) + (m - 1 - nc)

                if nr == n - 1 and nc == m - 1:
                    end_distance = cnt + 1

                q.append((nr, nc, cnt + 1))

    return gram_distance, end_distance


n, m, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# BFS를 통해 시작 지점에서 칼의 위치 및 목표 지점까지의 최단 거리를 계산
gram_distance, end_distance = bfs(0, 0)

# 칼을 사용하지 않거나 사용하여 도달한 최단 거리 중 작은 값 선택
ans = min(gram_distance, end_distance)

if ans <= t:
    print(ans)
else:
    print("Fail")
