X, Y, W, S = map(int, input().split())
if 2*W <= S:
    print((X+Y)*W)
else:
    answer = min(X, Y)*S
    absXY = abs(X-Y)
    if W > S:
        if absXY % 2 == 0:
            answer += absXY * S
        else:
            answer += (absXY-1)*S + W
    else:
        answer += absXY*W
    print(answer)