for t in range(1, int(input())+1):
    print(f'#{t}', end=' ')
    nums = sorted(map(int, input().split()), reverse=True)
    result = set()
    for i in range(5):
        for j in range(i+1, 7):
            for k in range(j+1, 7):
                result.add(nums[i]+nums[j]+nums[k])
    print(sorted(result)[-5])