n = int(input())

ans = 0
for _ in range(n):
    stack = []
    word = input()
    for i in word:
        if not stack:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    if not stack:
        ans += 1

print(ans)