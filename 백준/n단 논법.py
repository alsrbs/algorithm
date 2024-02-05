from collections import deque
import sys

input = sys.stdin.readline


def BFS(s, e):
    q = deque([s])
    result = 'F'
    while q:
        x = q.popleft()

        if x == e:
            result = 'T'
            break

        q += graph[x]

    print(result)
    return


n = int(input())
graph = [[] for _ in range(26)]

for _ in range(n):
    Premise1 = input()
    A = ord(Premise1[0]) - 97
    B = ord(Premise1[5]) - 97

    graph[A].append(B)

m = int(input())

for _ in range(m):
    Premise2 = input()
    S = ord(Premise2[0]) - 97
    E = ord(Premise2[5]) - 97

    BFS(S, E)
