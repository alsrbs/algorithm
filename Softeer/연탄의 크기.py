n = int(input())
yeontans = list(map(int, input().split()))

ans = 0
for i in range(2, max(yeontans)+1):
    c = 0
    for y in yeontans:
        if y%i == 0:
            c += 1

    ans = max(ans, c)

print(ans)