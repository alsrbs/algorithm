N = int(input())
nums = [0]+[int(input()) for i in range(N)]
dp = [0] * 301
if len(nums)<=2:
    print(sum(nums))
else:
    dp[0]=nums[0]
    dp[1]=nums[0]+nums[1]
    for i in range(2, N+1):
        dp[i]=max(dp[i-3]+nums[i-1]+nums[i], dp[i-2]+nums[i])
    print(dp[N])