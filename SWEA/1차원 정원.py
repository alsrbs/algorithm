for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    n, d = map(int, input().split())
    x = 2*d+1
    if n>x and n%x!=0:print(n//x+1)
    elif n>x and n%x==0:print(n//x)
    else:print(1)
