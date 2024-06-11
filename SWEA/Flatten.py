for t in range(1, 11):
    print(f'#{t}', end=' ')
    n = int(input())
    nums = list(map(int, input().split()))
    for i in range(n):
        nums[nums.index(max(nums))] -= 1
        nums[nums.index(min(nums))] += 1
        if set(nums)==1:break
    print(max(nums)-min(nums))