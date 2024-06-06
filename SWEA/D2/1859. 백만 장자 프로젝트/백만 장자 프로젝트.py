for i in range(1, int(input())+1):
    n = int(input())
    nums = list(map(int, input().split()))
    result = 0
    num = nums[-1]
    for j in range(n-2, -1, -1):
        if num > nums[j]:
            result += num-nums[j]
        else:
            num = nums[j]
    print(f'#{i} {result}')