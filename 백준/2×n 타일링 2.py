N = int(input())
dp = [1]*(N+1)
for i in range(2, N + 1):
    num = 1
    if i%2:num = -1
    dp[i] = ((dp[i-1] * 2) + num)%10007
print(dp[N])