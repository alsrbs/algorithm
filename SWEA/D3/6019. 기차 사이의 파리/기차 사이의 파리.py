for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    d, a, b, f = map(int, input().split())
    print(d/(a+b)*f)
