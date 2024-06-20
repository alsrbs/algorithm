nums = [0]*10001

for num in range(1, 10001):
    x = num + sum(list(map(int, str(num))))
    if x <= 10000:
        nums[x] = 1

for i in range(1, 10001):
    if not nums[i]:
        print(i)


