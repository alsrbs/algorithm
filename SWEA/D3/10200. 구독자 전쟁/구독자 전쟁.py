for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    n, a, b = map(int, input().split())
    result = [min(a, b), 0]
    if n<a+b:result[1]=a+b-n
    print(*result)