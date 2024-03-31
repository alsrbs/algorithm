from collections import deque

def solution(n, wires):
    dic = {i: [] for i in range(1, n+1)}
    
    for i in wires:
        dic[i[0]].append(i[1])
        dic[i[1]].append(i[0])
    
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
                return 0
            else:
                result.append(total)
                
    return min(result)