from collections import deque

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

q = deque([("ICN",["ICN"], [])])
result = []

while q:
    airport, path, res = q.popleft()

    if len(res) == len(tickets):
        result.append(path)

    for idx, ticket in enumerate(tickets):
        if ticket[0] == airport and idx not in res:
            q.append((ticket[1], path+[ticket[1]], res+[idx]))

result.sort()

print(result[0])