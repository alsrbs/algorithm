n, m = map(int, input().split())
S = [input() for _ in range(n)]

ans = 0
for _ in range(m):
    word = input()
    if word in S:
        ans += 1

print(ans)