import sys

input = sys.stdin.readline


N = int(input())
dp = list(map(int, input().split()))

for _ in range(N-1):
    money = list(map(int, input().split()))

    money[0] += min(dp[1], dp[2])
    money[1] += min(dp[0], dp[2])
    money[2] += min(dp[1], dp[0])
    dp = money[:]

print(min(dp))
