for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    n, k = map(int, input().split())
    ks = list(map(int, input().split()))
    result = []
    for i in range(1, n+1):
        if i not in ks:
            result.append(i)
    print(*result)