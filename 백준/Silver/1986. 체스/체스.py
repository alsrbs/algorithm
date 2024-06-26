def Q_check(x, y):

    # 가로 확인
    y1, y2 = y, y
    while True:
        y1 -= 1
        if 0<=y1<m and (chessboard[x][y1] == 0 or chessboard[x][y1] == 1):
            chessboard[x][y1] = 1
        else:
            break

    while True:
        y2 += 1
        if 0 <= y2 < m and (chessboard[x][y2] == 0 or chessboard[x][y2] == 1):
            chessboard[x][y2] = 1
        else:
            break

    # 세로
    x1, x2 = x, x
    while True:
        x1 -= 1
        if 0 <= x1 < n and (chessboard[x1][y] == 0 or chessboard[x1][y] == 1):
            chessboard[x1][y] = 1
        else:
            break

    while True:
        x2 += 1
        if 0 <= x2 < n and (chessboard[x2][y] == 0 or chessboard[x2][y] == 1):
            chessboard[x2][y] = 1
        else:
            break

    # 대각선
    x3, y3 = x, y
    while True:
        x3 -= 1
        y3 -= 1
        if 0<=x3 and 0<=y3 and (chessboard[x3][y3] == 0 or chessboard[x3][y3] == 1):
            chessboard[x3][y3] = 1
        else:
            break

    x4, y4 = x, y
    while True:
        x4 += 1
        y4 += 1
        if x4<n and y4<m and (chessboard[x4][y4] == 0 or chessboard[x4][y4] == 1):
            chessboard[x4][y4] = 1
        else:
            break

    x5, y5 = x, y
    while True:
        x5 -= 1
        y5 += 1
        if 0 <= x5 and y5<m and (chessboard[x5][y5] == 0 or chessboard[x5][y5] == 1):
            chessboard[x5][y5] = 1
        else:
            break

    x6, y6 = x, y
    while True:
        x6 += 1
        y6 -= 1
        if x6 < n and 0 <= y6 and (chessboard[x6][y6] == 0 or chessboard[x6][y6] == 1):
            chessboard[x6][y6] = 1
        else:
            break


def K_check(x, y):
    for i in [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]:
        nx = x + i[0]
        ny = y + i[1]

        if 0<=nx<n and 0<=ny<m and chessboard[nx][ny] == 0:
            chessboard[nx][ny] = 1


n, m = map(int, input().split())
chessboard = [[0]*m for _ in range(n)]
q_list = list(map(int, input().split()))
k_list = list(map(int, input().split()))
p_list = list(map(int, input().split()))

for i in range(1, len(q_list), 2):
    chessboard[q_list[i]-1][q_list[i+1]-1] = 'Q'

for i in range(1, len(k_list), 2):
    chessboard[k_list[i]-1][k_list[i+1]-1] = 'K'

for i in range(1, len(p_list), 2):
    chessboard[p_list[i]-1][p_list[i+1]-1] = 'P'

for i in range(n):
    for j in range(m):
        if chessboard[i][j] == 'Q':
            Q_check(i, j)
        elif chessboard[i][j] == 'K':
            K_check(i, j)

ans = 0
for i in chessboard:
    ans += i.count(0)

print(ans)