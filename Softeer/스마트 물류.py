n, k = map(int, input().split())
n_list = list(input())
ans = 0
# P: 로봇, H: 부품
for i in range(n):
    if n_list[i] == 'P':
        s = i-k
        e = i+k
        if s<0:
            s = 0
        if e>=n:
            e = n-1

        for j in range(s, e+1):
            if n_list[j] == 'H':
                n_list[j] = 'X'
                ans += 1
                break

print(ans)
