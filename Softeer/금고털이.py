import sys
input = sys.stdin.readline

w, n = map(int, input().split())
info = [tuple(map(int, input().split())) for _ in range(n)]

info.sort(key=lambda x:x[1], reverse=True)  # 가격이 높은 순으로 정렬

ans = 0
for m, p in info:
    if w-m>=0:
        w-=m
        ans += m*p
    else:
        ans += w*p
        break

print(ans)