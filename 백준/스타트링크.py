import sys
from collections import deque

input = sys.stdin.readline


def bfs(v):

    q = deque([v])

    while q:
        v = q.popleft()

        if v == G:
            return result[G]

        for i in (v + U, v - D):
            if 1 <= i <= F and i != S and not result[i]:
                result[i] = result[v] + 1
                q.append(i)

    if result[G] == 0:
        return 'use the stairs'


F, S, G, U, D = map(int, input().split())
if S == G:
    print(0)
else:
    result = [0] * (F + 1)
    print(bfs(S))
