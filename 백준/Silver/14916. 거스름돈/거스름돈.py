n = int(input())
ans = 0
for i in range(n//5, -1, -1):
    if (n - 5*i)%2 == 0:
        ans += i + (n-5*i)//2
        break
if ans:
    print(ans)
else:
    print(-1)