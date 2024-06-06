for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            total = 0
            for k in range(m):
                total += sum(arr[i+k][j:j+m])
            result = max(result, total)
    print(f'#{t} {result}')