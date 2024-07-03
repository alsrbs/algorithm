import sys
input = sys.stdin.readline

n = int(input())

stack = []
ans = 0
for _ in range(n):
    Homework = list(map(int, input().split()))

    if Homework[0] == 1:
        if Homework[2] == 1:
            ans += Homework[1]
        else:
            stack.append([Homework[1], Homework[2]-1])
        continue

    if stack:
        stack[-1][1] -= 1
        if stack[-1][1] == 0:
            h = stack.pop()
            ans += h[0]

print(ans)
