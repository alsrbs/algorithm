for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    sudoku_c = list(zip(*sudoku))
    result = 0
    for i in range(9):
        if len(set(sudoku[i]))==9:result+=1
        if len(set(sudoku_c[i])) == 9: result += 1

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            box = []
            box += sudoku[i][j:j+3] + sudoku[i+1][j:j+3] + sudoku[i+2][j:j+3]
            if len(set(box))==9:result+=1

    if result == 27:print(1)
    else:print(0)