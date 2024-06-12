for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    d, l, n = map(int, input().split())
    print(int(sum([d*(1+i*l*0.01) for i in range(n)])))