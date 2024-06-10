for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    P, Q, R, S, W = list(map(int, input().split()))
    x = Q
    if R < W:x += (W-R)*S
    print(min(P*W, x))