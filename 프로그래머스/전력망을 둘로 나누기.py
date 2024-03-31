from collections import deque

n = 7
wires = [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]

dic = {i: [] for i in range(1, n+1)}

for i in wires:
    dic[i[0]].append(i[1])
    dic[i[1]].append(i[0])

print(dic)

result = []
for i in range(1, n+1):
    for j in dic[i]:
        vis = [0]*(n+1)
        vis[i] = 1
        q = deque(dic[i])
        while q:
            x = q.popleft()
            if x == j:continue
            if vis[x] == 0:
                vis[x] = 1
                q += dic[x]
        total = abs(n-vis.count(1)*2)
        if total == 0:
            print(0)
            break
        else:
            result.append(total)

print(min(result))