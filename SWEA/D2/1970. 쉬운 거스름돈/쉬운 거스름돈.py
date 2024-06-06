for t in range(1, int(input())+1):
    print(f'#{t}')
    n = int(input())
    for money in [50000, 10000, 5000, 1000, 500, 100, 50, 10]:
        print(n//money, end=' ')
        n%=money
    print()