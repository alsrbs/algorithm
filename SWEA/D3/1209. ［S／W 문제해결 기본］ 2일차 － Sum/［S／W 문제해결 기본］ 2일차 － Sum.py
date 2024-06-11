for t in range(1, 11):
    n = int(input())
    print(f'#{n}', end=' ')
    arr = [list(map(int, input().split())) for _ in range(100)]
    arr_r = list(zip(*arr))
    result, s1, s2 = 0, 0, 0
    for i in range(100):
        s1 += arr[i][i]
        s2 += arr_r[i][99-i]
        result = max(sum(arr[i]), sum(arr_r[i]), result)
    print(max(result, s1, s2))
