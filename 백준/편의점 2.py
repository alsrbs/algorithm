import sys

input = sys.stdin.readline

n = int(input())
list_x = []
list_y = []

for _ in range(n):
    x, y = map(int, input().split())
    list_x.append(x)
    list_y.append(y)

list_x.sort()
list_y.sort()

mid_x, mid_y = list_x[n//2], list_y[n//2]

result = 0
for i in range(n):
    result += abs(list_x[i] - mid_x) + abs(list_y[i] - mid_y)

print(result)
