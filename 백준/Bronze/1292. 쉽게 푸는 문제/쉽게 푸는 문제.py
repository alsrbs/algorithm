a, b = map(int, input().split())
arr = []
for i in range(1, 46):
    arr += [i] * i
    if len(arr) >= b:
        break

print(sum(arr[a-1:b]))