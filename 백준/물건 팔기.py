N = int(input())
arr = []
for i in range(N):
    a, b = map(int, input().split())
    arr += [(a, b)]
arr.sort()

res = 0
target = 0
for i in range(N):
    c = 0
    for j in range(i, N):
        if arr[i][0] - arr[j][1] > 0:
            c += arr[i][0] - arr[j][1]
    if res < c:
        res = c
        target = arr[i][0]
print(target)