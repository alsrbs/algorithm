def solution(keyinput, board):
    dic = {'up': (0, 1), 'right': (1, 0), 'down': (0, -1), 'left': (-1, 0)}
    r, c = board[0]//2, board[1]//2
    
    for i in keyinput:
        dr, dc = dic[i]
        if 0 <= r + dr < board[0] and 0 <= c + dc < board[1]:
            r += dr
            c += dc
    return [r - board[0]//2, c - board[1]//2]