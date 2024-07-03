import sys
input = sys.stdin.readline

n = int(input())

storage = []
for _ in range(n):
    a, b = map(int, input().split())
    storage.append((a, b))

storage.sort()

# 가장 높은 기둥의 높이와 위치를 찾는다.
max_h = max(storage, key=lambda x: x[1])[1]
max_idx = next(i for i, v in enumerate(storage) if v[1] == max_h)

# 가장 높은 기둥의 넓이 추가
ans = max_h

# 왼쪽 부분 계산
h = storage[0][1]
for i in range(max_idx):
    if h < storage[i + 1][1]:
        ans += h * (storage[i + 1][0] - storage[i][0])
        h = storage[i + 1][1]
    else:
        ans += h * (storage[i + 1][0] - storage[i][0])

# 오른쪽 부분 계산
h = storage[-1][1]
for i in range(n - 1, max_idx, -1):
    if h < storage[i - 1][1]:
        ans += h * (storage[i][0] - storage[i - 1][0])
        h = storage[i - 1][1]
    else:
        ans += h * (storage[i][0] - storage[i - 1][0])

print(ans)
