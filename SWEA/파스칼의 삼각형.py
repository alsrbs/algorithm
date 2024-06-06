for t in range(1, int(input())+1):
    print(f'#{t}')
    n = int(input())
    for i in range(1, n+1):
        for j in range(i):
            if j == 0 or j == i-1:
                print(1, end=' ')
            else:
                print(i-1, end=' ')
        print()