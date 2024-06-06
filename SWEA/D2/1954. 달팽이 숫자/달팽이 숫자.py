for t in range(1, int(input())+1):
    print(f'#{t}')
    n = int(input())
    if n == 1:print(1);continue
    arr = [[0]*n for _ in range(n)]
    idx = 0
    r, c = 0, 0
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    arr[0][0]=1
    while True:
        nr = r + dr[idx]
        nc = c + dc[idx]
        if 0<=nr<n and 0<=nc<n and arr[nr][nc] == 0:arr[nr][nc] += arr[r][c]+1;r, c = nr, nc
        elif 0<=r + dr[(idx+1)%4]<n and 0<=c + dc[(idx+1)%4]<n and arr[r + dr[(idx+1)%4]][c + dc[(idx+1)%4]] != 0:break
        else:idx = (idx+1)%4

    for i in arr:
        print(*i)