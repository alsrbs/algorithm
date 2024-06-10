for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    nums = sorted(map(int, input().split()))
    x = nums.count(nums[0])
    print(nums[0] if x==3 or x==1 else nums[-1])
