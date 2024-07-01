from collections import deque

n , k = map(int, input().split())
q = deque([i for i in range(1, n+1)])

ans = []
while q:
    q.rotate(-k+1)
    x = q.popleft()
    ans.append(x)

print(f'<{", ".join(map(str, ans))}>')
