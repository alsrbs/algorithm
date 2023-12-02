def solution(n):
    dp = [0]*(n+1)
    for i in range(1, n+1):
        if i == 1:
            dp[i] = 1
        elif i == 2:
            dp[i] = 2
        elif i == 3:
            dp[i] = 3
        else: 
            dp[i] = (dp[i-1] + dp[i-2])%1234567
    # if n%2 != 0 and n>3:
    #     return dp[-1]-1
    # else:
    return dp[-1]