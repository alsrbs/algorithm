import sys
t = int(sys.stdin.readline())
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
for _ in range(t):
    order = list(map(str, sys.stdin.readline().strip()))
    direction = 0  # 북: 0 서: 1 남: 2 동: 3
    list_x, list_y = [0], [0]
    for i in order:
        if i == "F":
            list_x += [list_x[-1] + dx[direction]]
            list_y += [list_y[-1] + dy[direction]]
        elif i == "B":
            list_x += [list_x[-1] - dx[direction]]
            list_y += [list_y[-1] - dy[direction]]
        elif i == "L":
            if direction == 3:
                direction = 0
            else:
                direction += 1
        elif i == "R":
            if direction == 0:
                direction = 3
            else:
                direction -= 1
    list_x.sort()
    list_y.sort()
    print(abs(list_x[-1]-list_x[0])*abs(list_y[-1]-list_y[0]))
