money = 1000 - int(input())
coin = [500, 100, 50, 10, 5, 1]
ans = 0

for i in coin:
    x = money//i
    if x:
        ans += x
        money %= i
print(ans)
