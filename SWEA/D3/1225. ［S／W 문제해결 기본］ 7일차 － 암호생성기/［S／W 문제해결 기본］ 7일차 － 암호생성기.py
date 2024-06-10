for t in range(10):
    n = int(input())
    print(f'#{n}', end=' ')
    nums = list(map(int, input().split()))

    min_num = min(nums)
    if min_num>15:
        x = min_num//15-1
        for i in range(len(nums)):
            nums[i] -= 15*x

    t = 1
    while True:
        for i in range(len(nums)):
            if t == 6: t = 1
            nums[i] -= t
            if nums[i]<=0:
                t = False
                break
            t += 1

        if not t:break
    min_num_idx = nums.index(min(nums))
    print(*nums[min_num_idx+1:]+nums[:min_num_idx]+[0])