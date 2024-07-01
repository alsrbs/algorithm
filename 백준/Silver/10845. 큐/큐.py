import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    cmd = input().split()

    if cmd[0] == 'push':
        arr = [int(cmd[1])] + arr

    elif cmd[0] == 'pop':
        if arr:
            num = arr.pop()
            print(num)
        else:
            print(-1)

    elif cmd[0] == 'size':
        print(len(arr))

    elif cmd[0] == 'empty':
        if arr:
            print(0)
        else:
            print(1)

    elif cmd[0] == 'front':
        if arr:
            print(arr[-1])
        else:
            print(-1)

    elif cmd[0] == 'back':
        if arr:
            print(arr[0])
        else:
            print(-1)