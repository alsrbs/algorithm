for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    n = int(input())
    result = 0
    for i in range(1, n+1):
        if i%2 != 0:
            result += i
        else:
            result -= i
    print(result)