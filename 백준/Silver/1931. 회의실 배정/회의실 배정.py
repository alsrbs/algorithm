N = int(input())
lst = [tuple(map(int, input().split())) for _ in range(N)]
lst.sort()
lst.sort(key=lambda x: x[1])

a = total = 0
for i in range(1, N):
    if lst[a][1] <= lst[i][0]:
        a, total = i, total + 1
print(total + 1)