import re

expression = "100-200*300-500+20"
expression = re.split(r'([-+*])', expression)
arr = ['*+-', '*-+', '+-*', '+*-', '-+*', '-*+']
result = 0

for i in range(6):
    nums = expression[:]
    for j in range(3):

        k = 1
        while True:
            if k >= len(nums):break
            if arr[i][j] not in expression or arr[i][j] != nums[k]:
                k += 2
                continue

            num1 = int(nums.pop(k - 1))
            operator = nums.pop(k - 1)
            num2 = int(nums.pop(k - 1))

            if operator == '+':
                num = num1 + num2
            elif operator == '-':
                num = num1 - num2
            elif operator == '*':
                num = num1 * num2

            nums.insert(k - 1, num)

    result = max(abs(nums[0]), result)

print(result)


