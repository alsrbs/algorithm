for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    n, m = map(int, input().split())
    t, o = m, 0
    while t*2+o*1!=n:
        t, o = t-1, o+1
    print(o, t)