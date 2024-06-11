for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    a, b, c = map(int, input().split())
    print(c//min(a, b))