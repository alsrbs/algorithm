t = int(input())
for _ in range(t):
    n = int(input())
    word = input().split()

    ans = word[0]
    for i in range(1, n):
        
        if ans[0] == ans[-1]:
            if ans[-1] <= word[i]:
                ans += word[i]
            else:
                ans = word[i] + ans

        else:
            if ans[0] >= word[i]:
                ans = word[i] + ans
            else:
                ans += word[i]

    print(ans)