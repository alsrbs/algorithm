import math
from collections import deque

# 남 동 북 서
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

N, L, R = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def bfs(i,j):
    q = deque()
    q.append((i,j))
    vis[i][j] = True
    union = [(i,j)]
    cnt = arr[i][j]

    # 인접 국가를 탐색하며 차이가 L명 이상 R명 이하인 경우 담기
    while q:
        r,c = q.popleft()
        for k in range(4):
            nr = dr[k] + r
            nc = dc[k] + c
            if (0<=nr<N and 0<=nc<N) and not vis[nr][nc] and L<=abs(arr[nr][nc]-arr[r][c])<=R:
                union.append((nr,nc))
                vis[nr][nc] = True
                q.append((nr,nc))
                cnt += arr[nr][nc]

    for r, c in union:
        arr[r][c] = math.floor(cnt/len(union))  # 소수점 버리기

    return len(union)

result = 0  # 인구이동 발생 일수
while True:
    vis = [[False]*N for _ in range(N)]
    flag = False    # 인구 이동 존재 유무
    for i in range(N):
        for j in range(N):
            if not vis[i][j]:
                if bfs(i,j) > 1:
                    flag = True
    if not flag:    # 인구이동이 없을 경우
        break
    result += 1

print(result)