arr = [[1]*i for i in range(31)]

for i in range(2, 31):
    for j in range(1, i-1):
        arr[i][j] = arr[i-1][j-1] + arr[i-1][j]


r, c, w = map(int, input().split())

ans = 0
for i in range(r, r+w):
    for j in range(c-1, c+i-r):
        ans += arr[i][j]

print(ans)