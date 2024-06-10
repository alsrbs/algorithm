for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    a, b = map(int, input().split())
    print((a+b)%24)