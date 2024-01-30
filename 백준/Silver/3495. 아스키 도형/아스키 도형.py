h, w = map(int, input().split())
arr = [list(input()) for _ in range(h)]

result = 0
for i in range(h):
    x = 0
    for j in range(w):

        if arr[i][j] == '/' or arr[i][j] == '\\':
            x += 1

        if x % 2 == 1 and arr[i][j] == '.':
            result += 1

    result += x//2

print(result)