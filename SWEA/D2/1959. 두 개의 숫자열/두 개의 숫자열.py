for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    B_list, S_list = [], []
    if n>m:B_list, S_list = a, b
    else:B_list, S_list = b, a
    
    result = -9999
    for i in range(max(n, m)-min(n, m)+1):
        total = 0
        for j in range(min(n, m)):
            total += B_list[i+j]*S_list[j]
        result = max(result, total)
    print(result)