from collections import deque
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
def red_green_color_blindness(r, c, target):
    q = deque([(r, c)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nr = x + dr[i]
            nc = y + dc[i]
            if nr >= n or nc >= n or nr < 0 or nc < 0:continue
            if res[nr][nc]: continue
            if target in ['R', 'G']:
                if graph[nr][nc] == 'B':continue
            if target == 'B':
                if graph[nr][nc] in ['R', 'G']:continue
            q.append((nr, nc))
            res[nr][nc] = True
    return 1

def Not_red_green_color_blindness(r,c, target):
    q = deque([(r, c)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nr = x + dr[i]
            nc = y + dc[i]
            if nr >= n or nc >= n or nr < 0 or nc < 0: continue
            if Not_res[nr][nc]: continue
            if target != graph[nr][nc]:continue
            q.append((nr,nc))
            Not_res[nr][nc] = True
    return 1

n = int(input())
graph = [input() for i in range(n)]
res = [[False]*n for _ in range(n)]
Not_res = [[False]*n for _ in range(n)]
red_green_color_blindness_num = 0
Not_red_green_color_blindness_num = 0
for i in range(n):
    for j in range(n):
        if not res[i][j]:
            red_green_color_blindness_num += red_green_color_blindness(i,j, graph[i][j])
        if not Not_res[i][j]:
            Not_red_green_color_blindness_num += Not_red_green_color_blindness(i,j, graph[i][j])
print(Not_red_green_color_blindness_num, red_green_color_blindness_num)