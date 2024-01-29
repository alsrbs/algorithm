N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

row, col = 0, 0
r, c = 0, 0
for i in range(N):
    for j in range(M):
        x = arr[i][j] - r

        if x > 0:
            row += x

        r = arr[i][j]

    r = 0

for i in range(M):
    for j in range(N):
        x = arr[j][i] - c

        if x > 0:
            col += x

        c = arr[j][i]

    c = 0

print(row*2+col*2+N*M*2)
