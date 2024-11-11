n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n

for i in range(n-1, -1, -1):
    if i + arr[i] >= n - 1:
        dp[i] = 1
    else:
        dp[i] = dp[i + arr[i] + 1] + 1

print(*dp)