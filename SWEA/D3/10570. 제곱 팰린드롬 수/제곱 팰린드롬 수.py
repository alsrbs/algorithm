for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    a, b = map(int, input().split())
    c = 0
    for i in [1, 4, 9, 121, 484]:
        if a<=i<=b:c+=1
    print(c)