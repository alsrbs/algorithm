# 바이러스 수, 증가율, 시간
k, p, n = map(int, input().split())
dp = [0]*(n+1)
dp[0] = k
for i in range(1, n+1):
    dp[i] = (dp[i-1]*p)%1000000007
print(dp[n])
