def solution(board, h, w):
    W = len(board[0])
    H = len(board)
    target_color = board[h][w]
    dr = [0, 1, -1, 0]
    dc = [1, 0, 0, -1]
    cnt = 0
    for i in range(4):
        nr = w + dr[i]
        nc = h + dc[i]

        if nr < 0 or nc < 0 or nr >= W or nc >= H:continue
        if target_color == board[nc][nr]:
            cnt += 1
    return cnt