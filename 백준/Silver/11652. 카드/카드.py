import sys
input = sys.stdin.readline

n = int(input())
dic = {}

# 숫자의 빈도 계산
for _ in range(n):
    num = int(input())
    dic[num] = dic.get(num, 0) + 1

# 가장 큰 빈도수를 찾고, 빈도수가 같은 경우 가장 작은 숫자를 선택
max_freq = max(dic.values())
most_frequent_number = min(num for num, freq in dic.items() if freq == max_freq)

print(most_frequent_number)
