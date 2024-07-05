import sys
from collections import deque
input = sys.stdin.readline


n, k = map(int, input().split())
test_tube = []  # 시험관 상태를 저장할 리스트
virus_positions = []  # 각 바이러스의 초기 위치를 저장할 리스트

# 시험관 상태를 입력받고, 바이러스의 위치를 기록
for i in range(n):
    arr = list(map(int, input().split()))
    test_tube.append(arr)
    for j in range(n):
        if arr[j] != 0:
            virus_positions.append((arr[j], i, j))  # (바이러스 번호, 행, 열) 저장

# s: 시간, x: 목표 행, y: 목표 열
s, x, y = map(int, input().split())

# 바이러스 번호 순으로 정렬
virus_positions.sort()

# 큐 초기화, (바이러스 번호, 행, 열, 시간)을 저장
q = deque([(num, r, c, 0) for num, r, c in virus_positions])

# BFS 탐색 시작
while q:
    virus_num, r, c, time = q.popleft()

    if time == s:  # 주어진 시간이 되면 종료
        break

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc

        if 0 <= nr < n and 0 <= nc < n and test_tube[nr][nc] == 0:
            test_tube[nr][nc] = virus_num  # 바이러스로 감염
            q.append((virus_num, nr, nc, time + 1))  # 새로 감염된 위치 큐에 추가

# 목표 위치 (x, y)의 바이러스 상태 출력
print(test_tube[x-1][y-1])
