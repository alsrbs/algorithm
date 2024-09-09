n, m = map(int, input().split())
arr = [input() for _ in range(n)]
z_arr = list(zip(*arr))

r, c = 0, 0
for i in range(n):
    if 'X' not in arr[i]:
        r += 1

for i in range(m):
    if 'X' not in z_arr[i]:
        c += 1

print(max(r, c))