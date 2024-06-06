for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr_t = list(zip(*arr))
    result = 0
    for i in range(n):
        x_c, y_c = 0, 0
        for j in range(n):
            x_c += arr[i][j]
            y_c += arr_t[i][j]
            if not arr[i][j]:
                if x_c == k:result += 1
                x_c = 0
            if not arr_t[i][j]:
                if y_c == k:result += 1
                y_c = 0
        if x_c == k:result+=1
        if y_c == k:result+=1
    print(result)



