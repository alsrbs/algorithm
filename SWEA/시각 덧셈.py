for t in range(1, int(input())+1):
    h1, m1, h2, m2 = map(int, input().split())
    h = h1 + h2 + (m1+m2)//60
    m = (m1+m2)%60
    if h>12:h-=12
    print(f'#{t} {h} {m}')