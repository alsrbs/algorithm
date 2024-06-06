for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    m1, d1, m2, d2 = map(int, input().split())
    result = d2+(day[m1]-d1)+1
    if m1==m2:print(d2-d1+1)
    elif m1+1==m2:print(result)
    else:print(result+sum(day[m1+1:m2]))