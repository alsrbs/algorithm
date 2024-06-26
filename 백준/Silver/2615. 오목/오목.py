# 가로
def row_check(x, y, z):
    cnt = 1
    left_point = (x, y)

    y1 = y
    while True:
        y1 -= 1
        if 0<=y1<19 and arr[x][y1] == z:
            left_point = (x, y1)
            cnt+=1
        else:
            break

    y2 = y
    while True:
        y2 += 1
        if 0<=y2<19 and arr[x][y2] == z:
            cnt+=1
        else:
            break

    if cnt == 5:
        return left_point


# 세로
def col_check(x, y, z):
    cnt = 1
    left_point = (x, y)

    x1 = x
    while True:
        x1 -= 1
        if 0<=x1<19 and arr[x1][y] == z:
            left_point = (x1, y)
            cnt+=1
        else:
            break

    x2 = x
    while True:
        x2 += 1
        if 0<=x2<19 and arr[x2][y] == z:
            cnt+=1
        else:
            break

    if cnt == 5:
        return left_point


# 대각선
def dia1_check(x, y, z):
    cnt = 1
    left_point = (x, y)

    x1 = x
    y1 = y
    while True:
        x1 -= 1
        y1 -= 1
        if 0<=x1<19 and 0<=y1<19 and arr[x1][y1] == z:
            left_point = (x1, y1)
            cnt+=1
        else:
            break

    x2 = x
    y2 = y
    while True:
        x2 += 1
        y2 += 1
        if 0<=x2<19 and 0<=y2<19 and arr[x2][y2] == z:
            cnt+=1
        else:
            break

    if cnt == 5:
        return left_point


# 대각선
def dia2_check(x, y, z):
    cnt = 1
    left_point = (x, y)

    x1 = x
    y1 = y
    while True:
        x1 -= 1
        y1 += 1
        if 0<=x1<19 and 0<=y1<19 and arr[x1][y1] == z:
            cnt+=1
        else:
            break

    x2 = x
    y2 = y
    while True:
        x2 += 1
        y2 -= 1
        if 0<=x2<19 and 0<=y2<19 and arr[x2][y2] == z:
            left_point = (x2, y2)
            cnt+=1
        else:
            break

    if cnt == 5:
        return left_point


arr = [list(map(int, input().split())) for _ in range(19)]

for i in range(19):
    for j in range(19):
        if arr[i][j] != 0:
            rc = row_check(i, j, arr[i][j])
            cc = col_check(i, j, arr[i][j])
            d1c = dia1_check(i, j, arr[i][j])
            d2c = dia2_check(i, j, arr[i][j])

            for k in [rc, cc, d1c, d2c]:
                if k:
                    print(f'{arr[i][j]}\n{k[0]+1} {k[1]+1}')
                    exit()

print(0)