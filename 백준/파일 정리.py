n = int(input())
d = {}
for _ in range(n):
    w = input().split('.')[1]
    if w in d:
        d[w] += 1
    else:
        d[w] = 1
for i in sorted(d):
    print(f'{i} {d[i]}')