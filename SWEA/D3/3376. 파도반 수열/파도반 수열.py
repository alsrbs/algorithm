dp = [0] + [1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0]*90

for i in range(11, 101):
    dp[i] = dp[i-1] + dp[i-5]

for t in range(1, int(input())+1):
    print(f'#{t} {dp[int(input())]}')
