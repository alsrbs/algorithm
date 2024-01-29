N, K, B = map(int, input().split())
road = [0] * (N+1)

for _ in range(B):
    idx = int(input())
    road[idx] = 1

min_num = sum(road[1:K])
result = K
for i in range(1, N - K + 2):
    if road[i] == 1:
        min_num -= 1
    if road[i + K - 1] == 1:
        min_num += 1
    result = min(result, min_num)
print(result)