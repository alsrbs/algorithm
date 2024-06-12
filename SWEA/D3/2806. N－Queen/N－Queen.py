def dfs(i):
    global result
    if i==n:
        result+=1
        return

    for j in range(n):
        if v1[j]==v2[i+j]==v3[i-j]==0:
            v1[j]=v2[i+j]=v3[i-j]=1
            dfs(i+1)
            v1[j]=v2[i+j]=v3[i-j]=0


for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    n = int(input())
    result = 0
    v1 = [0]*n
    v2 = [0]*(2*n)
    v3 = [0]*(2*n)
    dfs(0)
    print(result)