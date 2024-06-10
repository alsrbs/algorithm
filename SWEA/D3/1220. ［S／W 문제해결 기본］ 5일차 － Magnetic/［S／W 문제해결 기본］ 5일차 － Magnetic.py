for t in range(1, 11):
    print(f'#{t}', end=' ')
    n = int(input())
    arr = [list(input().split()) for _ in range(n)]
    arr_t = list(zip(*arr))
    cnt = 0
    for i in arr_t:
        cnt += ''.join(i).replace('0', '').replace('12', '3').count('3')
    print(cnt)
