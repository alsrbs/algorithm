import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

ans = 0
for i in range(n):
    if arr[i] == 1:
        arr[i] = 1 - arr[i]
        if i+1 < n:
            arr[i+1] = 1 - arr[i+1]
        if i+2 < n:
            arr[i+2] = 1 - arr[i+2]
        ans += 1

print(ans)