n = int(input())
h_road = list(map(int, input().split()))
h_road.append(0)
s = h_road[0]
answer = []
for i in range(n):
    if h_road[i] >= h_road[i+1]:
        answer.append(h_road[i] - s)
        s = h_road[i+1]

print(max(answer))