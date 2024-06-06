for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    n = int(input())
    result, s = 0, 0
    for i in range(n):
        speed = list(map(int, input().split()))
        if speed[0]==1:s += speed[1]
        elif speed[0]==2:s -= speed[1]
        if s<=0:s=0
        result += s
    print(result)