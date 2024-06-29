def extent(x):
    return 3/2*x**2

for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    a, b = map(int, input().split())
    print(int(extent(a)//extent(b)))
