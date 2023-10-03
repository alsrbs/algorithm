n, m = map(int, input().split())
rice_cakes = list(map(int, input().split()))
s = 0
e = max(rice_cakes)

res = 0
while s<=e:
    total = 0
    mid = (s+e)//2
    for i in rice_cakes:
        if i > mid:
            total+= i-mid
    if total < m:
        e = mid - 1
    else:
        res = mid
        s = mid + 1
print(res)