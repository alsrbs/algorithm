k = int(input())

d = 1
while k > d:
    d *= 2

result = d

cnt = 0
while k > 0:
    if k >= d:
        k -= d
    else:
        d //= 2
        cnt += 1

print(result, cnt)