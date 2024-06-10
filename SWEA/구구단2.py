for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    a, b = map(int, input().split())
    if a>9 or b>9:print(-1)
    else:print(a*b)