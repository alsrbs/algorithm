while True:

    arr = input().split()
    if arr[0] == '0':
        break

    n = int(arr[0])
    nums = sorted(arr[1:])
    num1 = ''
    num2 = ''

    for i in range(n):
        if nums[i] != '0':
            num1 = nums[i]
            num2 = nums[i+1]
            nums = nums[:i] + nums[i+2:]
            break

    for i in range(len(nums)):
        if i%2 == 0:
            num1 += nums[i]
        else:
            num2 += nums[i]

    print(int(num1) + int(num2))
