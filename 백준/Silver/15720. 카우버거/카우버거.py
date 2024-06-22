a, b, c = map(int, input().split())
Burger = sorted(map(int, input().split()), reverse=True)
side = sorted(map(int, input().split()), reverse=True)
beverage = sorted(map(int, input().split()), reverse=True)

ans = 0
B, s, bev = 0, 0, 0
while B < a or s < b or bev < c:

    B_m, s_m, bev_m = 0, 0, 0
    if B >= a:
        B_m = 0
    else:
        B_m = Burger[B]

    if s >= b:
        s_m = 0
    else:
        s_m = side[s]

    if bev >= c:
        bev_m = 0
    else:
        bev_m = beverage[bev]

    B, s, bev = B+1, s+1, bev+1

    if 0 not in (B_m, s_m, bev_m):
        ans += B_m+s_m+bev_m - (B_m+s_m+bev_m)*0.1
    else:
        ans += B_m+s_m+bev_m

print(sum(Burger) + sum(side) + sum(beverage))
print(int(ans))