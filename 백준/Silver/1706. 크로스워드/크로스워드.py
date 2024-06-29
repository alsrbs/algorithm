n, m = map(int, input().split())

arr = [input() for _ in range(n)]
arr_t = list(zip(*arr))

ans = set()
for i in range(n):
    for j in arr[i].split('#'):
        if len(j) > 1:
            ans.add(j)

for i in range(m):
    for j in ''.join(arr_t[i]).split('#'):
        if len(j) > 1:
            ans.add(j)

print(sorted(ans)[0])