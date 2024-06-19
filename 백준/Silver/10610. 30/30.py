n = input()
nums = sorted(n, reverse=True)

if '0' in nums and sum(map(int, nums))%3==0:
    print(int(''.join(nums)))
else:
    print(-1)