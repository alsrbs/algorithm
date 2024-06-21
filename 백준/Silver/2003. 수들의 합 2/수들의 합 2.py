import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

l, r = 0, 1
ans = 0
while r<=n and l<=r:

    total = sum(nums[l:r])

    if total == m:
        ans += 1
        r += 1
    elif total < m:
        r+=1
    else:
        l+=1

print(ans)