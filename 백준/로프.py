import sys

input = sys.stdin.readline


n = int(input())
k = sorted([int(input()) for _ in range(n)], reverse=True)
ans = 0

for i in range(n):
    ans = max(ans, (i+1)*k[i])

print(ans)