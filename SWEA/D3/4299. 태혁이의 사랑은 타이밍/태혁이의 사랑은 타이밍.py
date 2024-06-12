for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    d, h, m = map(int, input().split())
    result = [11, 11, 11]
    if [d, h, m] == result:print(0)
    elif (d<=11 and h<=11 and m<11) or d<11 or (d<=11 and h<11) :print(-1)
    else:
        result[0] = (d-result[0])*24*60
        result[1] = (h-result[1])*60
        result[2] = m-result[2]
        print(sum(result))