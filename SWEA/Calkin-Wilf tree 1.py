for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    st=input()
    result = [1, 1]
    for i in st:
        if i=='L':result[1]+=result[0]
        else:result[0]+=result[1]
    print(*result)