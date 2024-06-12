for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    n, m = map(int, input().split())
    print('ON' if bin(m)[-n:] == '1'*n else 'OFF')

