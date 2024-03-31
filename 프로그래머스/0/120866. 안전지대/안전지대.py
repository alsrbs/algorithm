def solution(board):
    dr = [-1, -1, -1, 0, 0, 1, 1, 1]
    dc = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    board_x = len(board)
    board_y = len(board[0])
    
    total = board_x*board_y

    for i in range(board_x):
        for j in range(board_y):

            if board[i][j] == 1:
                x = 1
                for k in range(8):
                    nr = i + dr[k]
                    nc = j + dc[k]

                    if 0 <= nr < board_x and 0 <= nc < board_y and board[nr][nc] == 0:
                        board[nr][nc] = 'bomb'
                        x += 1

                total -= x
                
    return total