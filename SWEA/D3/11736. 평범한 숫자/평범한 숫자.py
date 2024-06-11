for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    n = int(input())
    nums = list(map(int, input().split()))
    result = 0
    for i in range(1, n-1):
        if nums[i] != max(nums[i], nums[i-1], nums[i+1]) and nums[i] != min(nums[i], nums[i-1], nums[i+1]):result+=1
    print(result)