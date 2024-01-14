nums = sorted(map(int, input().split()))
result = min(nums)
while True:
    c = 0
    for i in range(5):
        if result%nums[i]==0:
            c+=1
    if c>=3:
        print(result)
        break
    result += 1