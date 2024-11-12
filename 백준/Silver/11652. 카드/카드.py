n = int(input())
dic = {}

# 숫자의 빈도 계산
for _ in range(n):
    num = int(input())
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1

# 빈도수를 기준으로 내림차순 정렬하고, 빈도수가 같은 경우 숫자 오름차순으로 정렬
sorted_dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))

print(sorted_dic[0][0])