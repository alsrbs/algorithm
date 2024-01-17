import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
sum_nums = [0, nums[0]]
for i in range(2, n + 1):
    sum_nums += [sum_nums[i-1] + nums[i-1]]
m = int(input())
for _ in range(m):
    i, j = map(int, input().split())
    sys.stdout.write(str(sum_nums[j]-sum_nums[i-1])+"\n")
