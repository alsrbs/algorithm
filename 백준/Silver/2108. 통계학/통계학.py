from collections import Counter
import sys
input = sys.stdin.readline

def most_common_values(numbers):
    counter = Counter(numbers)
    most_common = counter.most_common()

    max_count = most_common[0][1] if most_common else 0
    most_common_values_list = [num for num, count in most_common if count == max_count]

    if len(most_common_values_list) == 1:
        return most_common_values_list[0]
    else:
        return most_common_values_list[1]

N = int(input())
nums = sorted(int(input()) for _ in range(N))

print(round(sum(nums)/N)) # 산술평균
print(nums[N//2]) # 중앙값
print(most_common_values(nums)) # 최빈값
print(nums[-1]-nums[0]) # 범위