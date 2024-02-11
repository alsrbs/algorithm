import sys
from collections import deque

input = sys.stdin.readline


A, B = map(int, input().split())
q = deque([[A, 1]])

while q:
    num, cnt = q.popleft()

    if num > B:continue
    if num == B:
        print(cnt)
        break
    q.append([num*2, cnt+1])
    q.append([int(str(num)+'1'), cnt+1])

else:
    print(-1)

