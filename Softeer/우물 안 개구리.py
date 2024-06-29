import sys

input = sys.stdin.readline

n, m = map(int, input().split())
w = [0] + list(map(int, input().split()))

friend = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)

ans = 0
for i in range(1, n + 1):
    # 친분 관계가 있는 회원
    flag = True
    for f in friend[i]:
        if w[i] <= w[f]:
            flag = False
            break

    if flag == True:
        ans += 1

print(ans)