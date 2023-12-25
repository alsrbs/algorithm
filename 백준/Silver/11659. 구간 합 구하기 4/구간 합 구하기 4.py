import sys

input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))
sum_nums = [0]
total = 0
for i in range(len(nums)):
    total += nums[i]
    sum_nums.append(total)

for _ in range(M):
    i, j = map(int, input().split())
    print(sum_nums[j] - sum_nums[i - 1])