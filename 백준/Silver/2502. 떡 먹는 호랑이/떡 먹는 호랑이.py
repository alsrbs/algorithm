D, K = map(int, input().split())

list_x = [1]*(D+1)
list_y = [1]*(D+1)
if D > 3:
    list_y[4] = 2
    if D > 4:
        for i in range(5, D+1):
            list_x[i] = list_x[i-1] + list_x[i-2]
            list_y[i] = list_y[i-1] + list_y[i-2]


z = K//list_y[D]
res = []
for i in range(z, 1, -1):
    c = 1
    while True:
        if c > i or list_x[-1]*c + list_y[-1]*i > K:break
        if K == list_x[-1]*c + list_y[-1]*i:
            res.append((c, i))
            break
        c += 1
    if res:break

print(res[0][0])
print(res[0][1])
