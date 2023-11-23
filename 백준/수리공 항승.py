N, L = map(int, input().split())
target_list = sorted(map(int, input().split()))

cnt = 1
start = target_list[0]
for i in target_list[1:]:
    if (i+0.5)-(start-0.5)<=L:
        continue
    else:
        start = i
        cnt += 1
print(cnt)