import sys

input = sys.stdin.readline

n = int(input())
customer = sorted([int(input()) for _ in range(n)], reverse=True)

ans = 0
for i in range(n):
    num = customer[i]-i
    if num>0:
        ans+=num
print(ans)