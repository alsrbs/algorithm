import sys, heapq

input = sys.stdin.readline

n = int(input())
nums = []

for _ in range(n):
    num = int(input())

    if num == 0:
        if nums:
            min_abs_value, min_value = heapq.heappop(nums)
            print(min_value)
        else:
            print(0)
    else:
        heapq.heappush(nums, (abs(num), num))
