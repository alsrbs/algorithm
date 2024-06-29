h, w = map(int, input().split())
arr = [list(input()) for _ in range(h)]
move = [(1, 0), (0, -1), (-1, 0), (0, 1)]
start = None
for i in range(h):
    for j in range(w):
        if arr[i][j] == '#':
            c = 0
            for k in range(4):
                ni = i + move[k][0]
                nj = j + move[k][1]

                if 0<=ni<h and 0<=nj<w and arr[ni][nj] == '#':
                    start = k
                    c+=1

            if c == 1:
                print(i, j, start)