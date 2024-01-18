N = int(input())
d = {i: [] for i in range(1, N+1)}
song = 0
E = int(input())
for i in range(E):
    K = list(map(int, input().split()))
    if 1 in K[1:]:
        song += 1
        for k in K[1:]:
            d[k] += [song]
    if song > 0 and 1 not in K[1:]:
        result_list = []
        for k in K[1:]:result_list += d[k]
        for j in K[1:]:d[j] += list(set(result_list))

for k, v in d.items():
    if song == len(set(v)):
        print(k)