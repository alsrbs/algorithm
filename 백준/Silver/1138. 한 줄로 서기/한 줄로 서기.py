n = int(input())
arr = list(map(int, input().split()))
ans = []
for i in range(n-1, -1, -1):
    ans.insert(arr[i], i+1)
print(*ans)