import sys

input = sys.stdin.readline

for t in range(int(input())):

    nums = list(map(int, input().split()))
    cnt = 0
    for i in range(1, len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                cnt += 1

    print(nums[0], cnt)