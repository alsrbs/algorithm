n, m = map(int, input().split())
arr = [0]*101

x = 0
for _ in range(n):
    dis, h = map(int, input().split())
    for i in range(1, dis+1):
        arr[i+x] = h
    x += dis

x = 0
ans = set()
for _ in range(m):
    dis, h = map(int, input().split())
    for i in range(1, dis + 1):
        n_h = h-arr[i + x]
        if n_h > 0:  # 제한속도를 벗어난 경우
            ans.add(h-arr[i + x])
        else:  # 제한속도를 벗어나지 않은 경우
            ans.add(0)
    x += dis

print(sorted(ans)[-1])