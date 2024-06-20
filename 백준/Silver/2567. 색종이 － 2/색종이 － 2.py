n = int(input())
arr = [[0]*101 for _ in range(101)]

for i in range(n):
    x, y = map(int, input().split())

    for j in range(x, x+10):
        for k in range(y, y+10):
            arr[j][k] = 1

ans = 0

for i in range(101):
    for j in range(101):
        if arr[i][j] == 1:
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if arr[i+x][j+y] == 0:
                    ans+=1

print(ans)