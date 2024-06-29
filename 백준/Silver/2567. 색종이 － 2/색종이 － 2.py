import sys

input = sys.stdin.readline


n = int(input())
arr = [[0]*101 for _ in range(101)]
list_x = []
list_y = []
for i in range(n):
    x, y = map(int, input().split())
    list_x.append(x)
    list_y.append(y)

    for j in range(x, x+10):
        for k in range(y, y+10):
            arr[j][k] = 1

list_x.sort()
list_y.sort()

ans = 0
for i in range(list_x[0], list_x[-1]+10):
    for j in range(list_y[0], list_y[-1]+10):
        if arr[i][j] == 1:
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if arr[i+x][j+y] == 0:
                    ans+=1

print(ans)