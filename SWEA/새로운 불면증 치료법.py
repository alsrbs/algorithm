for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    n = int(input())
    d = []
    i = 1
    while True:
        d += list(str(i*n))
        if len(set(d)) == 10:break
        i += 1
    print(i*n)
