E, S, M = 16, 29, 20
lst = list(map(int, input().split()))
target = 0

while True:
    if [target%E, target%S, target%M] == lst:
        break
    target += 1

print(target)

