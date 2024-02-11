import sys

input = sys.stdin.readline


def DFS(k, num, idx):
    if len(num) == 6:
        result.append(num)
        return

    for i in range(idx, k):
        if vis[i] == 0:
            vis[i] = 1
            DFS(k, num + [S[i]], i)
            vis[i] = 0


cnt = 0
while True:
    cnt += 1
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        exit()
    S = nums[1:]

    result = []
    for i in range(nums[0] - 6 + 1):
        vis = [0] * nums[0]
        vis[i] = 1
        DFS(nums[0], [S[i]], i)

    if cnt > 1:
        print()
    for i in result:
        print(*i)

