import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
current = [0] * n

ans = 0
for i in range(n):
    if arr[i] != current[i]:
        current[i] = not current[i]
        if i+1 < n:
            current[i+1] = not current[i+1]
        if i+2 < n:
            current[i+2] = not current[i+2]
        ans += 1

print(ans)