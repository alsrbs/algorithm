for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    L, U, X = list(map(int, input().split()))
    if U<X:print(-1)
    elif L<=X<=U:print(0)
    else:print(L-X)