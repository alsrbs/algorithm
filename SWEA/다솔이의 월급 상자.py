for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    n = int(input())
    result = 0
    for _ in range(n):
        fl, es = map(float, input().split())
        result += fl*es
    print(result)
