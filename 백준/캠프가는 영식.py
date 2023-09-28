N, T = map(int, input().split())
res = []
for i in range(N):
    t, d, n = map(int, input().split())
    if t+d*(n-1) < T:
        continue
    li = [t + d * i for i in range(n)]
    s, e = 0, n - 1
    a = 0
    while s <= e:
        m = (s+e)//2
        if li[m] >= T:
            a = m
            e = m-1
        else:
            s = m+1
    res.append(li[a]-T)
print(min(res) if res else -1)