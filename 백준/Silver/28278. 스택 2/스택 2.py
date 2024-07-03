import sys
input = sys.stdin.readline

n = int(input())

stack = []
l = 0
for _ in range(n):
    cmd = list(map(int, input().split()))

    if cmd[0] == 1:
        stack.append(cmd[1])
        l += 1

    elif cmd[0] == 2:
        if l:
            num = stack.pop()
            l -= 1
            print(num)
        else:
            print(-1)

    elif cmd[0] == 3:
        print(l)

    elif cmd[0] == 4:
        if l:
            print(0)
        else:
            print(1)

    else:
        if l:
            print(stack[-1])
        else:
            print(-1)
