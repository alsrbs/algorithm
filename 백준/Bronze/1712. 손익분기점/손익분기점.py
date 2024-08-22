a, b, c = map(int, input().split())
if b >= c:
    print(-1)
else:
    x = c - b
    answer = a // x + 1
    print(answer)