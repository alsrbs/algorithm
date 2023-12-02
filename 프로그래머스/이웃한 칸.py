board = [["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]]
h = 1; w = 1
W = len(board[0])
H = len(board)
target_color = board[h][w]
dr = [0, 1, -1, 0]
dc = [1, 0, 0, -1]
cnt = 0
for i in range(4):
    nr = w + dr[i]
    nc = h + dc[i]

    if nr < 0 or nc < 0 or nr >= W or nc >= H: continue
    if target_color == board[nc][nr]:
        cnt += 1
print(cnt)