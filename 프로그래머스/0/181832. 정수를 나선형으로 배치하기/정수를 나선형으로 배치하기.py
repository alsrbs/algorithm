def solution(n):
    answer = [[0]*n for _ in range(n)]
    answer[0][0] = 1
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    r, c = 0, 0
    
    for i in range(n * 2 - 1):
        while 0 <= r + dr[i % 4] < n and 0 <= c + dc[i % 4] < n and answer[r+dr[i % 4]][c+dc[i % 4]] == 0:
            r += dr[i % 4]
            c += dc[i % 4]
            answer[r][c] = answer[r - dr[i % 4]][c - dc[i % 4]] + 1
                
    return answer