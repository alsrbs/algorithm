a, b, c = map(int, input().split())
Burger = sorted(map(int, input().split()), reverse=True)
side = sorted(map(int, input().split()), reverse=True)
beverage = sorted(map(int, input().split()), reverse=True)

min_l = min(a, b, c)
ans = 0

for i in range(min_l):
    ans += (Burger[i] + side[i] + beverage[i])*0.9

ans += sum(Burger[min_l:]) + sum(side[min_l:]) + sum(beverage[min_l:])

print(sum(Burger) + sum(side) + sum(beverage))
print(int(ans))