import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ab_point = []

for i in range(n):
    if 1 in arr[i]:
        for j in range(m):
            if arr[i][j] == 1:
                ab_point.append((i, j))

print(abs(ab_point[1][0] - ab_point[0][0]) + abs(ab_point[1][1] - ab_point[0][1]))