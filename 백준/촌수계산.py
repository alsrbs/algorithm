from collections import deque
n = int(input()) # 전체 사람의 수
P1, P2 = map(int, input().split())
m = int(input())
P_list = [[] for _ in range(n+1)]
check = [0]*(n+1)

for _ in range(m):
    x, y = map(int, input().split())
    P_list[x] += [y]
    P_list[y] += [x]

q = deque([P1])
while q:
    a = q.popleft()
    for i in P_list[a]:
        if check[i] == 0:
            check[i] = check[a] + 1
            q.append(i)
print(check[P2] if check[P2] > 0 else -1)
