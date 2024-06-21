n = int(input())
dp = [0]*n
dp[0] = float(input())

for i in range(1, n):
    f = float(input())
    dp[i] = max(dp[i-1]*f, f)

print('%0.3f' % max(dp))