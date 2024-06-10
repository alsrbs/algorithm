for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    n = int(input())
    cnt = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if n**2 >= i**2 + j**2:
                cnt+=1
    print(cnt*4+1+n*4)