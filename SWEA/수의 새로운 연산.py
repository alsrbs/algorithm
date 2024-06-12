arr = [[0]*300 for _ in range(300)]
arr[0][0] = 1
for i in range(1, 300):
    arr[i][0] = arr[i-1][0]+i

for i in range(0, 300):
    for j in range(1, 300):
        arr[i][j] = arr[i][j-1]+1+j+i


for t in range(1, int(input())+1):
    print(f'#{t}',end=' ')
    num1, num2 = map(int, input().split())
    x, y, z, w = 0, 0, 0, 0

    for i in range(300):
        if num1 in arr[i]:
            y = arr[i].index(num1)
            x = i
        if num2 in arr[i]:
            w = arr[i].index(num2)
            z = i
        if x and y and z and w:break

    print(arr[x+z+1][y+w+1])
