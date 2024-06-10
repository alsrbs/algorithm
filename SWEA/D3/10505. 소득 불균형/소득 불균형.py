for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    n = int(input())
    nums = list(map(int, input().split()))
    cnt = 0
    for i in nums:
        if sum(nums)//n>=i:
            cnt+=1
    print(cnt)