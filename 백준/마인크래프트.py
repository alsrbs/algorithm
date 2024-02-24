import sys

input = sys.stdin.readline

N, M, B = map(int, input().split())
graph = {}

for _ in range(N):
    for i in list(map(int, input().split())):
        if i in graph:
            graph[i] += 1
        else:
            graph[i] = 1

sum_num = B
for key, value in graph.items():
    sum_num += key*value


high = max(graph.keys())
low = min(graph.keys())
short_time = int(1e9)
ground = 0
for i in range(low, high + 1):
    inven, plant = 0, 0

    if sum_num < i * N * M:continue

    for key, value in graph.items():
        if key > i:
            inven += (key - i) * value
        else:
            plant += (i - key) * value

    if inven + B < plant:
        continue
    else:
        time = (inven * 2) + plant
        if short_time >= time:
            short_time = time
            ground = i

print(short_time, ground)