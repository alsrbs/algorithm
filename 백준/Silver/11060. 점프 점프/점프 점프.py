import sys
from collections import deque

input = sys.stdin.readline


n = int(input())
a_list = list(map(int, input().split()))

if n == 1:
    print(0)
else:
    vis = [0]*(n+1)
    q = deque([1])

    while q:
        idx = q.popleft()

        if idx + a_list[idx - 1] >= n:
            print(vis[idx]+1)
            exit()

        for i in range(1, a_list[idx - 1] + 1):
            new_idx = i + idx

            if vis[new_idx] == 0:
                vis[new_idx] = vis[idx] + 1
                q.append(new_idx)

    print(-1)