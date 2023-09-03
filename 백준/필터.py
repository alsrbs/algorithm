r, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
t = int(input())
num = 0
for i in range(r):
    for j in range(c):
        if i+2<r and j+2<c:
            num1 = arr[i][j]
            num2 = arr[i][j+1]
            num3 = arr[i][j+2]
            num4 = arr[i+1][j]
            num5 = arr[i+1][j+1]
            num6 = arr[i+1][j+2]
            num7 = arr[i+2][j]
            num8 = arr[i+2][j+1]
            num9 = arr[i+2][j+2]
            lst = sorted([num1, num2, num3, num4, num5, num6, num7, num8, num9])
            if t <= lst[4]:
                num += 1
print(num)
