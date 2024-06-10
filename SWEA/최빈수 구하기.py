for t in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    d = {}
    for i in nums:
        if i in d:d[i]+=1
        else:d[i]=1
    print(f'#{n} {sorted(d.items(), key=lambda x:(-x[1], -x[0]))[0][0]}')