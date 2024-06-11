for t in range(1, 11):
    print(f'#{t}', end=' ')
    n = int(input())
    building = list(map(int, input().split()))
    result = 0
    for i in range(2, n-2):
        mxh = max(building[i-2], building[i-1], building[i+1], building[i+2])
        if building[i]-mxh>0:result+=building[i]-mxh
    print(result)