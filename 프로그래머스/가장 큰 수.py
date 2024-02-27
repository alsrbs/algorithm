nums = list(map(int, input().split()))

sorted_nums = sorted(nums, key=lambda x: str(x)*4, reverse=True)
result = str(int(''.join(map(str, sorted_nums))))
print(result)