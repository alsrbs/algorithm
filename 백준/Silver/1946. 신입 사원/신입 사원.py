import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n)]

    arr.sort()

    ans = 1
    top = 0
    for i in range(1, n):
        if arr[i][1] < arr[top][1]:
            ans += 1
            top = i

    print(ans)
