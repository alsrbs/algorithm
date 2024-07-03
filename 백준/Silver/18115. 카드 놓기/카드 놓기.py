import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
q = deque()

for i in range(n-1, -1, -1):
    num = n-i

    if arr[i] == 1:
        q.appendleft(num)
    elif arr[i] == 2:
        q.insert(1, num)
    else:
        q.append(num)

print(*q)