import re

def solution(expression):
    expression = re.split(r'([-+*])', expression)
    arr = ['*+-', '*-+', '+-*', '+*-', '-+*', '-*+']
    l = len(expression)
    result = []

    for i in range(6):
        nums = expression[:]
        for j in range(3):

            k = 1

            while True:
                if k >= len(nums):break

                if arr[i][j] not in expression:
                    k += 2
                    continue

                if arr[i][j] == nums[k]:
                    num1 = int(nums.pop(k - 1))
                    operator = nums.pop(k - 1)
                    num2 = int(nums.pop(k - 1))


                    if operator == '+':
                        x = num1 + num2

                    elif operator == '-':
                        x = num1 - num2

                    elif operator == '*':
                        x = num1 * num2

                    nums.insert(k - 1, x)

                else:
                    k += 2

        result.append(abs(nums[0]))

    return max(result)