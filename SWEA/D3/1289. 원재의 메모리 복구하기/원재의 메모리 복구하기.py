for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    n = input()
    cnt = 0
    if n[0]=='1':cnt+=1
    for i in range(1, len(n)):
        if n[i-1]!=n[i]:cnt+=1
    print(cnt)