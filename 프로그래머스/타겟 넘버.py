def dfs(numbers, target, idx, values):
    global cnt

    if idx == len(numbers):
        if values == target:
            cnt += 1
            return
        else:
            return

    dfs(numbers, target, idx+1, values + numbers[idx])
    dfs(numbers, target, idx+1, values - numbers[idx])



numbers = list(map(int, input().split()))
target = int(input())
cnt = 0
dfs(numbers, target, 0, 0)
print(cnt)
