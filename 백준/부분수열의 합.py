import sys
input = sys.stdin.readline


n, s = map(int, input().split())
nums = list(map(int, input().split()))

answer = 0


def subset_sum(idx, sub_sum):
    global answer

    if idx >= n:
        return

    sub_sum += nums[idx]

    if sub_sum == s:
        answer += 1

    subset_sum(idx + 1, sub_sum)
    subset_sum(idx + 1, sub_sum - nums[idx])


subset_sum(0, 0)
print(answer)