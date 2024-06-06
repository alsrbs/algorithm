for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    nums = sorted(map(int, input().split()))
    print(int(round((sum(nums)-nums[0]-nums[-1])/(len(nums)-2), 0)))