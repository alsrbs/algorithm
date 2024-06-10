for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    n = int(input())
    farm = [list(map(int, list(input()))) for _ in range(n)]
    if n==1:print(*farm[0])
    else:
        mid = n//2
        up, do, l, r = mid-1, mid+1, 1, n-1
        result = sum(farm[mid])
        while True:
            result += sum(farm[up][l:r])
            result += sum(farm[do][l:r])
            if up == 0:break
            up, do, l, r = up-1, do+1, l+1, r-1
        print(result)