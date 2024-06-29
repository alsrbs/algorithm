for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    a, b = map(int, input().split())
    ans = 0
    for i in range(a//b):
        ans += i*2 + 1
    print(ans)