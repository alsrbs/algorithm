n = int(input())
tteokguk = list(map(int, input().split()))
tteokguk_cnt = {}

for i in tteokguk:
    tteokguk_cnt[i] = tteokguk_cnt.get(i, 0) + 1

ans = sorted(tteokguk_cnt.items(), key=lambda x:-x[1])
print(ans[0][1])