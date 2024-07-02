import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

arr.sort()

ans = 0
for i in range(n):
    ans += abs(i+1 - arr[i])

print(ans)